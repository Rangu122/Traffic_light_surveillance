# Traffic-Light Surveillance 🚦

## Project Overview

Traffic-Light Surveillance is an AI-based traffic monitoring prototype that detects vehicles from a traffic video and monitors traffic activity.

The system uses **YOLOv8** for vehicle detection and **OpenCV** for video processing. It detects vehicles such as cars, buses, trucks, and motorcycles, counts them, and displays the current traffic status.

## Features

* 🚗 Vehicle detection
* 🚌 Bus detection
* 🚛 Truck detection
* 🏍️ Motorcycle detection
* 🔢 Vehicle counting
* 🚦 Traffic activity monitoring
* 📊 Low, Medium, and Heavy Traffic classification
* 🎥 Processed video output

## Technologies Used

* **Python**
* **YOLOv8**
* **OpenCV**
* **Google Colab**

## Model Used

**YOLOv8 Nano (YOLOv8n)**

YOLOv8 is used to detect objects in each frame of the traffic video.

The project focuses on these vehicle classes:

* Car
* Bus
* Truck
* Motorcycle

## Working Approach

1. A traffic video is provided as input.
2. The YOLOv8 model processes the video frame by frame.
3. Vehicles are detected using bounding boxes.
4. The detected vehicles are counted.
5. Based on the vehicle count, traffic activity is classified as:

   * Low Traffic
   * Medium Traffic
   * Heavy Traffic
6. The processed video is saved as `traffic_final.mp4`.

## Traffic Classification

| Vehicle Count | Traffic Status |
| ------------- | -------------- |
| 0–10          | Low Traffic    |
| 11–20         | Medium Traffic |
| More than 20  | Heavy Traffic  |

## Project Structure

```text
Traffic-Light-Surveillance/
│
├── traffic_surveillance.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## Running the Project

### Step 1: Download YOLOv8

The model can be loaded using:

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
```

### Step 2: Provide the Traffic Video

Place the traffic video in the project folder and use:

```python
video_path = "traffic.avi"
```

### Step 3: Run the Program

```bash
python traffic_surveillance.py
```

### Step 4: View the Output

After processing, the output video will be saved as:

```text
traffic_final.mp4
```

The output contains vehicle bounding boxes, vehicle count, and traffic status.

## Output

The system produces a processed traffic video showing:

* Detected vehicles
* Bounding boxes around vehicles
* Vehicle count
* Traffic status

## Future Improvements

With more development time, the project can be improved by adding:

* Traffic-light color detection
* Red-light violation detection
* Accident detection
* Number-plate recognition
* Emergency vehicle detection
* Real-time CCTV camera support
* Automatic traffic signal control

## Conclusion

This project demonstrates how computer vision and YOLOv8 can be used to build a simple AI-based traffic monitoring system. It provides vehicle detection, counting, and traffic activity monitoring from a video feed.
