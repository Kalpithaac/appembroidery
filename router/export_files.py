from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from services.export_dst import export_to_dst
from services.export_exp import export_to_exp
from services.export_pes import export_to_pes
from services.export_jef import export_to_jef
from services.export_tbf import export_to_tbf

router = APIRouter()

@router.post("/export")
def export_format(stitch_points: list, format: str):
    if format == "dst":
        data = export_to_dst(stitch_points)
    elif format == "exp":
        data = export_to_exp(stitch_points)
    elif format == "pes":
        data = export_to_pes(stitch_points)
    elif format == "jef":
        data = export_to_jef(stitch_points)
    elif format == "tbf":
        data = export_to_tbf(stitch_points)
    else:
        return {"error": "Unsupported format"}

    return StreamingResponse(
        iter([data]),
        media_type="application/octet-stream",
        headers={
            "Content-Disposition":
            f"attachment; filename=design.{format}"
        }
    )
