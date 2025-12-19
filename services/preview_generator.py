from PIL import Image, ImageDraw
import io

def generate_preview_image(fill_pts, border_pts, scale=4):

    xs = [p[0] for p in fill_pts+border_pts]
    ys = [p[1] for p in fill_pts+border_pts]

    min_x,max_x = min(xs), max(xs)
    min_y,max_y = min(ys), max(ys)

    w = (max_x - min_x)*scale + 40
    h = (max_y - min_y)*scale + 40

    img = Image.new("RGB",(w,h),(255,255,255))
    draw = ImageDraw.Draw(img)

    # fill red
    for (x,y) in fill_pts:
        sx = (x-min_x)*scale + 20
        sy = (y-min_y)*scale + 20
        draw.point((sx,sy),fill=(255,0,0))

    # satin border black
    for (x,y) in border_pts:
        sx = (x-min_x)*scale + 20
        sy = (y-min_y)*scale + 20
        draw.point((sx,sy),fill=(0,0,0))

    buf = io.BytesIO()
    img.save(buf,format="PNG")
    return buf.getvalue()
