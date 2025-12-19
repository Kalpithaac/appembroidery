import numpy as np
import cv2

def gen_stitch_points(edge_map):

    contours, _ = cv2.findContours(edge_map, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    points = []
    for cnt in contours:
        for p in cnt[::5]:  # sample every 5 pixels (stitch point)
            x, y = p[0]
            points.append((x, y))

    return points
