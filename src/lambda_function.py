import json
from video_splitter import split_video_to_frames, upload_frames_to_s3
import boto3
import os
import subprocess


lambda_client = boto3.client('lambda')

def lambda_handler(event, context):
    #if os.path.exists("/opt/bin"):
    #    print("Contents of /opt/bin:", os.listdir("/opt/bin"))

    #try:
    #    result = subprocess.run(
    #        ["/opt/bin/ffmpeg", "-version"],
    #        capture_output=True,
    #       text=True,
    #        check=True
    #    )
    #    print("FFmpeg output:", result.stdout)
    #except Exception as e:
    #    print("Error executing ffmpeg:", str(e))

    try:
        input_bucket = event['Records'][0]['s3']['bucket']['name']
        input_key = event['Records'][0]['s3']['object']['key']
        output_bucket = "1225462862-stage-1"

        # Split the video into frames
        frame_dir = split_video_to_frames(input_bucket, input_key)

        # Upload frames to S3 and get the frame name
        frame_name = upload_frames_to_s3(frame_dir, output_bucket)

        #Invoke the face-recognition function asynchronously
        #Uncomment this section if face-recognition functionality is ready
        invocation_payload = {
             "bucket_name": output_bucket,
             "image_file_name": frame_name,
             "result_bucket_name": "1225462862-output"
         }
        lambda_client.invoke(
             FunctionName="face-recognition",
             InvocationType="Event",  # Asynchronous invocation
             Payload=json.dumps(invocation_payload)
        )

        return {
            "statusCode": 200,
            "body": "Video successfully split, uploaded, and face-recognition triggered."
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": str(e)
        }
