# 🖐️ Virtual Mouse using Hand Gestures

A computer vision-based Virtual Mouse that allows users to control their computer cursor using hand gestures captured through a webcam. The project uses MediaPipe for hand tracking, OpenCV for image processing, and PyAutoGUI for controlling mouse actions.

## 🚀 Features

* Cursor movement using finger gestures
* Left-click gesture
* Right-click gesture
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

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/virtual-mouse.git
cd virtual-mouse
```

### 2. Install Required Packages

```bash
pip install opencv-python mediapipe pyautogui
```

---

## ▶️ Run the Project

```bash
python Virtual_mouse.py
```

Make sure your webcam is connected and accessible.

---

## 🎮 Gesture Controls

| Gesture                                     | Action            |
| ------------------------------------------- | ----------------- |
| Index Finger + Middle Finger close together | Move Cursor       |
| Thumb + Index Finger touch                  | Left Click        |
| Thumb + Middle Finger touch                 | Right Click       |
| Middle Finger + Ring Finger close together  | Scroll            |
| Thumb + Ring Finger touch                   | Show Desktop      |
| All Fingers Folded                          | Close Application |

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
* Internet connection (for initial package installation)

---

## Future Improvements

* Multi-hand support
* Drag and drop gesture
* Gesture customization
* Smoother cursor tracking
* Machine learning-based gesture recognition
* Cross-platform optimization

---

## 📸 Demo

Add screenshots, GIFs, or a demo video here to showcase the project.

---

## 👨‍💻 Author

Megh Patel

Developed as a Computer Vision and Human-Computer Interaction project using OpenCV and MediaPipe.

---

## 📄 License

This project is open-source and available under the MIT License.
