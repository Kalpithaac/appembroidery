import cv2
import numpy as np
from sklearn.cluster import KMeans
from config.settings import settings

def extract_colors(image_bytes):

    # read bytes → numpy → BGR image
    img_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # reshape to pixels
    pixels = img.reshape(-1, 3)

    # cluster into dominant colors
    kmeans = KMeans(
        n_clusters=settings.default_kmeans_colors,
        random_state=42,
        n_init="auto"
    )
    kmeans.fit(pixels)

    centers = kmeans.cluster_centers_  

    # return RGB not BGR
    return [tuple(map(int, c[::-1])) for c in centers]
