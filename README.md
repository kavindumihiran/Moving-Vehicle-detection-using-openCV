# 🚶‍♂️Moving-Vehicle-detection-using-openCV

This code demonstrate how to detect moving objects in a video a **static survailance camera** using only classical computer vision techniques. This system is capable of identifying motion, removing shadows, and drawing bounding boxes around moving vehicles. 

## 📌 Introduction

Detecting moving objects(vehicles) in a static camera setup is a fundamental task in video surveillance and traffic monitoring In this project, OpenCV's background subtraction, morphological operations and contour detection algorithms are used to detect and highlight moving objects in a video stream. 

## ⚙️ Project Functionality

The main functionality of the project includes:
- Reading a video feed from a surveillance camera or video file
- Applying background subtraction to detect motion
- Using morphological operations to clean noise
- Removing shadows using mask filtering
- Drawing bounding boxes around detected moving objects
- Displaying the final output with bounding boxes on moving objects

## ✨ Features

- 📹 Works with any video from a static surveillance camera
- 💡 Shadow removal for better accuracy
- 📦 Bounding boxes for real-time object visualization
- 🧹 Noise reduction with morphological operations

## ▶️ How to Run

### Requirements

- Python 3.x
- OpenCV (`opencv-python`)

### Installation

```bash
pip install opencv-python
```

### Run the Script

```bash
python motionDetection.py
```

## 📸 Example Output
A bounding box is drawn around each moving object:












