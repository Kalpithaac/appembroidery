import cv2
import numpy as np

def detect_edges(image_bytes):
    arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    edges = cv2.Canny(img, 80, 150)
    return edges
