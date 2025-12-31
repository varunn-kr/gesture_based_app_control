# Hand Gesture Controlled Application Opener (IP Camera)

A computer vision–based project that uses a **mobile phone as an IP camera** to detect **hand gestures** and control applications on a **Windows laptop** in real time.

The system recognizes the number of fingers shown and maps each gesture to a predefined desktop action such as opening or closing applications.



## Features

- Uses **phone camera** (IP Webcam) instead of laptop webcam
- Real-time **hand landmark detection**
- Finger-count–based gesture recognition
- Opens and closes desktop applications
- Stable gesture detection with controlled execution speed
- Lightweight and easy to extend



## Gesture Mapping

| Gesture (Fingers) | Action |

| 0 | Close currently active application |
| 1 | Open YouTube |
| 2 | Open YouTube Music |
| 3 | Open Brave Browser |

*(Gesture–action mapping can be customized in the code)*



## Tech Stack

- **Python 3**
- **OpenCV**
- **MediaPipe Hands**
- **PyAutoGUI**
- **IP Webcam (Android)**



## How It Works

1. Phone streams live video using IP Webcam
2. Laptop receives the stream via OpenCV
3. MediaPipe detects hand landmarks
4. Finger states are calculated using landmark positions
5. Recognized gesture triggers a desktop action



## Requirements

### Hardware
- Android smartphone
- Windows laptop
- Common Wi-Fi network

### Software

Install required Python libraries:


pip install opencv-python mediapipe pyautogui numpy

Setup & Usage
Step 1: Start IP Webcam

  i) Install IP Webcam from Play Store
  ii) Start the server
 iii) Copy the video URL (example):
           (http://192.168.1.10:8080/video)


Step 2: Update Camera URL
   In the Python script:
      IP_CAMERA_URL = "http://YOUR_PHONE_IP:8080/video"


Step 3: Run the Project
       python main.py

ENSURE: Phone and laptop are on the same network
        Adequate lighting for better hand detection

Accuracy Improvements Used:
        Landmark-based finger detection
        Action delay to prevent rapid triggers
        Single-hand tracking for stability
        Threshold-based gesture confirmation

Limitations
       Requires good lighting
       Designed for single-hand gestures
       IP camera latency depends on network quality

Future Improvements
      CNN-based gesture classification
      Custom gesture training
      Multi-hand support
      Computer vision mini-projects

Use Cases:
      Touchless desktop control
      Assistive technology
      Human–Computer Interaction projects
      Computer vision mini-projects
      Academic demonstrations


