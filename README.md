# 🖐️ Virtual Mouse using Hand Gestures

A computer vision-based Virtual Mouse that allows users to control their computer cursor using hand gestures captured through a webcam. The project uses MediaPipe for hand tracking, OpenCV for image processing, and PyAutoGUI for controlling mouse actions.

## 🚀 Features

* Cursor movement using finger gestures
* Left-click gesture
* Right-click gesture
* Middle-click gesture
* Scroll up/down using hand movement
* Show Desktop shortcut gesture
* Close application gesture
* Real-time hand tracking
* FPS monitoring
* Gesture recognition display

---

## 🛠️ Technologies Used

* Python 3.x
* OpenCV
* MediaPipe
* PyAutoGUI
* Threading
* Math

---

## ▶️ Run the Project

```bash
python Virtual_mouse.py
```

Make sure your webcam is connected and accessible. Close any other applications that are using the webcam.

---

## 🎮 Gesture Controls

| Gesture                                     | Action          |
| ------------------------------------------- | ----------------|
| Index Finger + Middle Finger close together | Move Cursor     |
| Thumb + Index Finger touch                  | Left Click      |
| Thumb + Middle Finger touch                 | Right Click     |
| Thumb + Ring Finger touch                   | Show Desktop    |
| Thumb + Pinky Finger touch                  | Middle Click    |
| Middle Finger + Ring Finger close together  | Scroll          |
| All Fingers Folded                          | Close Programm  |

---

## 🧠 How It Works

1. Webcam captures live video frames.
2. MediaPipe detects hand landmarks in real time.
3. Distances between specific finger landmarks are calculated.
4. Different gesture combinations trigger different mouse actions.
5. PyAutoGUI executes the corresponding system mouse commands.

---

## 📂 Project Structure

```text
virtual-mouse/
│
├── Virtual_mouse.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Requirements

* Windows 10/11
* Python 3.8+
* Webcam

---

## 🖱️ Mouse Functions Supported

This project supports all primary mouse functions:

* Cursor Movement
* Left Click
* Right Click
* Middle Click
* Scroll Wheel

---

## Future Improvements

* Gesture customization
* Smoother cursor tracking
* Machine learning-based gesture recognition

---

## 👨‍💻 Author

**Megh Patel**

Developed as a Computer Vision and Human-Computer Interaction project using OpenCV, MediaPipe, and PyAutoGUI.
