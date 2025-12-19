def export_to_tbf(points):

    stitches = bytearray()

    last = points[0]

    for px,py in points[1:]:
        dx = px-last[0]
        dy = py-last[1]
        stitches.extend(bytes([
            dx & 0xFF,
            dy & 0xFF
        ]))
        last=(px,py)

    return stitches
