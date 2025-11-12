import os
from fastapi import UploadFile
from io import BytesIO
# Get the bucket name from environment variables (recommended for Cloud Run)
GCS_BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME", "eval-jobs")
from google.cloud import storage

async def upload_file_to_gcs(file: UploadFile, excel_data: BytesIO, destination_blob_name: str):
    """Uploads a file to Google Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(destination_blob_name)
    # file_bytes = await file.read()
    # excel_data = BytesIO(file_bytes)
    # Reset the cursor to 0 before pandas reads it
    # excel_data.seek(0)
    blob.upload_from_file(excel_data, content_type=file.content_type)
    print(f"File {file.filename} uploaded to {destination_blob_name}.")

def download_file_from_gcs(source_blob_name: str, destination_file_path: str):
    """Downloads a file from Google Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_path)
    print(f"File {source_blob_name} downloaded to {destination_file_path}.")