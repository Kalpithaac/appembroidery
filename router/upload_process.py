from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

import cv2
import numpy as np

from services.azure_blob import upload_blob
from services.stitch_fill import generate_fill_stitches
from services.satin_border import generate_border_stitches
from services.stitch_optimizer import remove_jump_stitches
from services.preview_generator import generate_preview_image
from services.export_dst import export_to_dst
from services.stitch_estimator import estimate_stitches


router = APIRouter()


@router.post("/upload-process")
async def upload_and_process(file: UploadFile = File(...)):

    # read uploaded file
    file_bytes = await file.read()

    # convert to cv2 image
    np_img = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    if img is None:
        return JSONResponse({"error": "Invalid image file"}, status_code=400)

    # convert to binary mask for fill
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

    # tatami fill stitches
    fill_stitches = generate_fill_stitches(mask, step=4)

    # detect edges for satin border
    edges = cv2.Canny(mask, 40, 120)

    border_stitches = generate_border_stitches(edges, width=3, spacing=3)

    # merge stitches
    stitch_points = fill_stitches + border_stitches

    # remove long jump stitches
    stitch_points = remove_jump_stitches(stitch_points, max_jump=12)

    # generate preview image optionally
    preview_bytes = generate_preview_image(
        fill_stitches,
        border_stitches,
        scale=4
    )

    preview_url = upload_blob(preview_bytes, f"{file.filename}-preview.png")

    # export dst embroidery binary
    dst_bytes = export_to_dst(stitch_points)

    dst_url = upload_blob(dst_bytes, f"{file.filename}.dst")

    # compute stats
    stats = estimate_stitches(stitch_points)

    return {
        "previewUrl": preview_url,
        "dstUrl": dst_url,
        "totalStitches": stats["total_stitches"],
        "estimatedTime": stats["est_time"],
        "density": stats["density"],
        "dimensions": stats["dimensions"]
    }
