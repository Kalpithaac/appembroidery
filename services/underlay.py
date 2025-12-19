def generate_underlay(mask, step=8):
    stitches = []
    h,w = mask.shape

    for y in range(0,h,step):
        inside=False
        for x in range(w):
            if mask[y,x]>0:
                if not inside:
                    inside=True
                    start=x
                last=x
            else:
                if inside:
                    stitches.append((start,y))
                    stitches.append((last,y))
                    inside=False
        if inside:
            stitches.append((start,y))
            stitches.append((last,y))
    return stitches
