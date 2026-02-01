# Gesture Controlled Virtual Mouse 🖐️🖱️

A real-time gesture-controlled virtual mouse system using a webcam.  
The project allows users to control mouse movement and actions using hand gestures without any physical mouse.

## Features
- Cursor movement using hand gestures
- Left click & right click
- Scroll up/down
- Show desktop (Win + D)
- Safe exit gesture
- Smooth performance with gesture filtering

## Technologies Used
- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## How It Works
- Webcam captures live video
- MediaPipe detects hand landmarks
- Finger distance-based gestures are recognized
- Mouse actions are executed using PyAutoGUI

## How to Run
1. Install required libraries:
   - pip install opencv-python mediapipe pyautogui
2. Run the program

## Use Case
This project demonstrates Human–Computer Interaction (HCI) using Computer Vision and can be useful for hands-free system control.

## Author
Megh Patel
