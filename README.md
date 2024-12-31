# Video Analysis PaaS Application

## Overview
This project implements a scalable, serverless video analysis application using AWS Lambda and supporting services such as S3. The application processes uploaded videos through a multi-stage pipeline, splitting the videos into frames and performing face recognition on extracted frames using a pre-trained ResNet-34 model. The results are stored in an output bucket, enabling seamless video processing in a cost-effective and elastic manner.

## Features
### Core Functionalities
1. **Video Splitting**:
   - Splits videos into frames using FFmpeg.
   - Stores extracted frames in an intermediate S3 bucket.

2. **Face Recognition**:
   - Detects faces in frames using the SSD algorithm.
   - Identifies faces using ResNet-34-based embeddings compared against pre-stored data.
   - Saves recognized names in an output S3 bucket as text files.

3. **Serverless Architecture**:
   - Uses AWS Lambda to handle function execution for each stage of the pipeline.
   - Dynamically scales based on workload.

4. **Cloud Storage**:
   - Employs S3 buckets to store video files, frames, and results.

### Workflow
1. User uploads a video to the input bucket.
2. A Lambda function splits the video into frames and stores them in the stage-1 bucket.
3. Another Lambda function processes the frames for face recognition, saving results as text files in the output bucket.

## Technologies Used
- **AWS Lambda**: Serverless function execution.
- **AWS S3**: Data storage for videos, frames, and results.
- **FFmpeg**: Video processing and frame extraction.
- **OpenCV**: Face detection in images.
- **PyTorch**: ResNet-34-based face recognition.
- **Python**: Primary language for Lambda functions.
- **Docker**: To containerize the face recognition Lambda function.

## Project Structure
- **Input Bucket**:
  Stores the uploaded video files.
- **Stage-1 Bucket**:
  Stores extracted frames from the video files.
- **Output Bucket**:
  Stores text files with recognized face names.

## Setup Instructions
- AWS CLI configured with credentials.
- Python 3.7 or later installed locally.

### Deployment
1. **Deploy the Video Splitting Lambda Function**:
   - Write the function in the Lambda UI or use the provided `video-splitting-cmdline.py`.
   - Use FFmpeg as an external library.

2. **Deploy the Face Recognition Lambda Function**:
   - Build the function using `handler.py` and `Dockerfile`.
   - Add required Python libraries (e.g., OpenCV, PyTorch) to the Docker container.
   - Reduce image size using lightweight base images like `python:3.7-slim`.

3. **Create S3 Buckets**:
   - `Input-bucket-1`: For video uploads.
   - `stage-1`: For storing extracted frames.
   - `output-bucket`: For storing recognized face results.

## References
- The **video splitting Lambda function** is based on the example provided in the project:
  [Video Splitting Code](https://github.com/visa-lab/CSE546-Cloud-Computing/blob/main/Project_2/src/video-splitting-cmdline.py).
- The **face recognition Lambda function** is adapted from:
  [Face Recognition Code](https://github.com/visa-lab/CSE546-Cloud-Computing/blob/main/Project_2/src/face-recognition-code.py).
- The **dataset** used for testing is referenced from:
  [Dataset Test Case](https://github.com/visa-lab/CSE546-Cloud-Computing/tree/main/Project_2/dataset/test_case_2).




