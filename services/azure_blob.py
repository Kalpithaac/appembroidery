from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
from config.settings import settings
import uuid
import re

client = BlobServiceClient.from_connection_string(settings.azure_blob_conn)
container = client.get_container_client(settings.azure_blob_container)

# extract account key manually from connection string
def get_account_key():
    match = re.search(r'AccountKey=([^;]+)', settings.azure_blob_conn)
    if match:
        return match.group(1)
    raise Exception("AccountKey not found in connection string")

def upload_blob(data: bytes, filename: str):
    blob_name = f"{uuid.uuid4()}-{filename}"
    blob_client = container.get_blob_client(blob_name)
    blob_client.upload_blob(data, overwrite=True)

    account_key = get_account_key()

    sas_token = generate_blob_sas(
        account_name=client.account_name,
        container_name=settings.azure_blob_container,
        blob_name=blob_name,
        account_key=account_key,                         # FIX HERE
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=2)
    )

    return f"{blob_client.url}?{sas_token}"
