#__copyright__   = "Copyright 2024, VISA Lab"
#__license__     = "MIT"

from boto3 import client as boto3_client
from s3_face_recognition import process_image
import json
import os

def handler(event, context):
    """
    Lambda handler function.
    """
    try:
        # Extract bucket name and file name from the event payload
        bucket_name = event.get("bucket_name")
        image_file_name = event.get("image_file_name")
        result_bucket_name = event.get("result_bucket_name")

        if not bucket_name or not image_file_name or not result_bucket_name:
            raise ValueError("Missing required parameters: bucket_name, image_file_name, or result_bucket_name")

        print(f"Received event: {event}")

        # Call the helper function to process the image
        process_image(bucket_name, image_file_name, result_bucket_name)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Processing completed successfully"})
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
