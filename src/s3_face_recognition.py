import boto3
import os
import json
from face_recognition_code import face_recognition_function

# Initialize S3 client
s3_client = boto3.client('s3')
DATA_BUCKET = 'project-3-data-bucket'
DATA_PT_KEY = 'data.pt'


def download_file_from_s3(bucket_name, file_name, local_folder="/tmp"):
    """
    Downloads a file from S3 to the local temp directory.
    """
    local_path = os.path.join(local_folder, file_name)
    s3_client.download_file(bucket_name, file_name, local_path)
    print(f"Downloaded {file_name} from bucket {bucket_name} to {local_path}")
    return local_path

def upload_result_to_s3(bucket_name, file_name, content):
    """
    Uploads a result to an S3 bucket.
    """
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=content
    )
    print(f"Uploaded result to bucket {bucket_name} with key {file_name}")

def process_image(bucket_name, image_file_name, result_bucket_name):
    """
    Handles the complete process of downloading, processing, and uploading results.
    """
    # Step 1: Download the file from S3
    local_path = download_file_from_s3(bucket_name, image_file_name)

    # Step 2: Process the file using the face recognition function
    if not os.path.exists("/tmp/data.pt"):
        print(f"Downloading {DATA_PT_KEY} from bucket {DATA_BUCKET} to {local_path}")
        download_file_from_s3(DATA_BUCKET, DATA_PT_KEY)
        print("Download complete.")
    else:
        print(f"{local_path}/data.pt already exists locally.")

    result = face_recognition_function(local_path)

    # Step 3: Upload the result to the result S3 bucket
    result_k = image_file_name.split('.')[0]
    print(f"result_k {result_k}")
    result_key = f"{result_k}.txt"
    print(f"result_key {result_key}")
    upload_result_to_s3(result_bucket_name, result_key, result)

    print(f"Processing completed for {image_file_name}, result uploaded to {result_key}")
