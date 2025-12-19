# services/export_dst.py

def export_to_dst(stitch_points):

    dst = bytearray()

    # 512-byte header padded with spaces
    header = b"LA:design.dst".ljust(512, b'\x20')
    dst.extend(header)

    last_x, last_y = 0, 0

    for (x, y) in stitch_points:

        dx = x - last_x
        dy = y - last_y

        # simple placeholder encoding:
        #   1 byte dx
        #   1 byte dy
        #   1 byte flag (normal stitch)
        dst.extend(bytes([
            dx & 0xFF,
            dy & 0xFF,
            0x03
        ]))

        last_x, last_y = x, y

    # End-of-file command required for DST
    dst.extend(bytes([0, 0, 0xF3]))

    return bytes(dst)          # IMPORTANT

