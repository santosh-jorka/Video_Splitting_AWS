import os
import subprocess
import boto3

s3_client = boto3.client('s3')

def split_video_to_frames(input_bucket, input_key):
    """
    Downloads the video from S3 and splits it into frames locally.
    Returns the directory path where frames are stored.
    """
    # Create temporary file paths
    input_file_path = f"/tmp/{os.path.basename(input_key)}"
    output_dir_path = f"/tmp/{os.path.splitext(os.path.basename(input_key))[0]}"
    os.makedirs(output_dir_path, exist_ok=True)

    # Download the video file from S3
    s3_client.download_file(input_bucket, input_key, input_file_path)

    

    ffmpeg_binary_path = "/opt/bin/ffmpeg"
    ffmpeg_command = [
        ffmpeg_binary_path, "-i", input_file_path, "-vframes", "1",
        f"{output_dir_path}/{os.path.splitext(os.path.basename(input_key))[0]}.jpg", "-y"
    ]

    # Run the ffmpeg command
    try:
        subprocess.run(ffmpeg_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running ffmpeg: {e}")
        raise Exception("Error in processing video with ffmpeg.")

    # Clean up the input video file (but not the frames directory)
    os.remove(input_file_path)
    print("split successfull")
    return output_dir_path  # Return directory containing frames


def upload_frames_to_s3(frame_dir, output_bucket):
    """
    Uploads frames from a local directory to the specified S3 bucket.
    Returns the name of the uploaded frame.
    """
    # Ensure the directory exists
    if not os.path.exists(frame_dir):
        raise Exception(f"Frame directory {frame_dir} does not exist.")

    frame_name = None

    for frame in os.listdir(frame_dir):
        frame_path = os.path.join(frame_dir, frame)
        frame_name = os.path.basename(frame_path)  # Capture frame name for return
        s3_client.upload_file(frame_path, output_bucket, frame_name)

    # Clean up frames after uploading
    for frame in os.listdir(frame_dir):
        os.remove(os.path.join(frame_dir, frame))
    os.rmdir(frame_dir)
    print("frame name successfull")
    return frame_name  # Return the name of the last uploaded frame
