def export_to_jef(points):

    header = bytearray(128)   # JEF fixed header block
    data = bytearray()

    last = points[0]

    for p in points[1:]:
        dx = p[0] - last[0]
        dy = p[1] - last[1]

        data.append(dx & 0xFF)
        data.append(dy & 0xFF)

        last = p

    return header + data
