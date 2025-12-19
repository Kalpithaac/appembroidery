def export_to_pes(points):

    pes = bytearray()

    pes.extend(b"#PES0001")       # PES signature

    # placeholder section length
    pes.extend((0).to_bytes(4,"little"))

    last = points[0]

    for px,py in points[1:]:
        dx = px-last[0]
        dy = py-last[1]

        pes.extend(dx.to_bytes(2,"little",signed=True))
        pes.extend(dy.to_bytes(2,"little",signed=True))

        last=(px,py)

    return pes
