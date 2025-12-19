import cv2
import numpy as np

def generate_border_stitches(edge_map, width=3, spacing=3):
    """
    Satin border stitch generator.
    Creates repeated needle passes along the contour edges.
    """

    contours, _ = cv2.findContours(
        edge_map,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE
    )

    stitch_points = []

    for cnt in contours:

        cnt = cnt.squeeze()

        for i in range(0, len(cnt), spacing):

            x, y = cnt[i]

            # duplicate border stitch passes
            for w in range(-width, width + 1):
                stitch_points.append((x + w, y))

    return stitch_points
