import cv2
import numpy as np

def generate_fill_stitches(mask, step=4):
    """
    Generate tatami fill stitches for filled embroidery regions.
    mask : 2D binary mask (255 inside shape, 0 outside)
    """

    stitches = []

    h, w = mask.shape

    for y in range(0, h, step):
        inside = False

        for x in range(w):

            if mask[y, x] > 0:               # inside stitched region
                if not inside:
                    inside = True
                    start_x = x
                last_x = x
            else:
                if inside:
                    inside = False
                    stitches.append((start_x, y))
                    stitches.append((last_x, y))

        if inside:
            # close open segment at end edge
            stitches.append((start_x, y))
            stitches.append((last_x, y))

    return stitches

