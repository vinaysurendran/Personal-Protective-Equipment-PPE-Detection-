# Personal Protective Equipment (PPE) Detection

## Overview
This project implements a real-time Personal Protective Equipment (PPE) detection system using the YOLO (You Only Look Once) object detection model. It can detect whether individuals are wearing safety equipment such as hard hats, masks, and safety vests, and identify those who are not compliant with safety regulations.

## Features
- Uses the **YOLO model** for fast and accurate object detection.
- Detects various PPE items including **Hardhat, Mask, Safety Vest**.
- Identifies non-compliance (e.g., **NO-Hardhat, NO-Mask, NO-Safety Vest**).
- Draws bounding boxes with color-coded alerts:
  - **Red**: Non-compliance (No PPE)
  - **Green**: Compliance (Wearing PPE)
  - **Blue**: Other objects detected (e.g., vehicles, machinery)
- Real-time detection using a webcam.

## Requirements
Make sure you have the following dependencies installed before running the project:

- Python 3.x
- OpenCV
- Ultralytics YOLO
- NumPy
- Torch
- CUDA (optional for GPU acceleration)

### Install Dependencies
```sh
pip install opencv-python ultralytics torch numpy
```

## Usage
### 1. Load the YOLO Model
Ensure you have the **ppe.pt** model file downloaded and specify its path in the script.

```python
modelpath = r"C:\Users\vinay\Code\Python files\ppe\ppe.pt"
model = YOLO(modelpath)
```

### 2. Run the Script
Execute the Python script to start real-time detection:
```sh
python ppe_detection.py
```

### 3. Exit the Program
Press **'q'** on your keyboard to quit the detection window.

## Model Classes
The YOLO model is trained to detect the following classes:
- Hardhat
- Mask
- NO-Hardhat
- NO-Mask
- NO-Safety Vest
- Person
- Safety Cone
- Safety Vest
- Machinery
- Vehicle

## Customization
- To use a **video file** instead of a webcam, modify:
  ```python
  cap = cv2.VideoCapture("path_to_video.mp4")
  ```
- Adjust confidence threshold to control detection sensitivity.

## Acknowledgments
- **Ultralytics YOLO** for providing a robust object detection framework.
- OpenCV for real-time image processing.

## License
This project is open-source and can be modified for non-commercial use.

