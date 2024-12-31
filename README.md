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
   - Employs S3 buckets to store video files, frames, and output data.

### Workflow
1. User uploads a video to the input bucket (`<ASU ID>-input`).
2. A Lambda function splits the video into frames and stores them in the stage-1 bucket (`<ASU ID>-stage-1`).
3. Another Lambda function processes the frames for face recognition, saving results as text files in the output bucket (`<ASU ID>-output`).

## Technologies Used
- **AWS Lambda**: Serverless function execution.
- **AWS S3**: Data storage for videos, frames, and results.
- **FFmpeg**: Video processing and frame extraction.
- **OpenCV**: Face detection in images.
- **PyTorch**: ResNet-34-based face recognition.
- **Python**: Primary language for Lambda functions.
- **Docker**: To containerize the face recognition Lambda function.

## Project Struct
