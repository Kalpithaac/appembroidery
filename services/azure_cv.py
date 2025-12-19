import requests
from config.settings import settings

def analyze_with_azure_cv(image_bytes):

    headers = {
        "Ocp-Apim-Subscription-Key": settings.azure_cv_key,
        "Content-Type": "application/octet-stream"
    }

    params = {"visualFeatures": "Color,Objects,Description"}

    response = requests.post(
        settings.azure_cv_endpoint + "/vision/v3.2/analyze",
        headers=headers,
        params=params,
        data=image_bytes
    )

    return response.json()
