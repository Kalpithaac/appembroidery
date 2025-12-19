def export_to_exp(points):

    data = bytearray()

    last = points[0]

    for p in points[1:]:
        dx = int(p[0] - last[0])
        dy = int(p[1] - last[1])

        data.extend(bytes([dx & 0xFF, dy & 0xFF]))

        last = p

    return data
