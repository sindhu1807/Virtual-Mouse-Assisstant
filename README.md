Virtual Mouse Using Hand Gestures

This project enables mouse control using hand gestures detected via webcam. It utilizes MediaPipe for hand tracking, OpenCV for video processing, and PyAutoGUI to control the system mouse. It supports cursor movement, left and right clicks, scrolling, and screenshots, based on hand gestures.

Features

- Move the mouse cursor using the index finger
- Left click with a thumb + index finger pinch
- Right click with a thumb + middle finger pinch
- Scroll up with a thumb + ring finger pinch
- Scroll down with a thumb + pinky finger pinch
- Take a screenshot using an open palm gesture

Technologies Used

- Python 3.x
- MediaPipe
- OpenCV
- PyAutoGUI
- NumPy

How It Works

- The webcam feed is captured and processed in real-time.
- MediaPipe detects hand landmarks.
- Hand gestures are interpreted based on the relative positions of the fingers.
- PyAutoGUI is used to control the mouse and perform actions.

Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/virtual-mouse-gestures.git
cd virtual-mouse-gestures
````

2. Install the required packages:

```bash
pip install opencv-python mediapipe pyautogui numpy
```

3. Run the script:

```bash
python virtual_mouse.py
```

To exit the program, press the `Esc` key.

Gesture Reference

| Gesture                     | Action          |
| --------------------------- | --------------- |
| Index finger up             | Move cursor     |
| Thumb + Index finger pinch  | Left click      |
| Thumb + Middle finger pinch | Right click     |
| Thumb + Ring finger pinch   | Scroll up       |
| Thumb + Pinky finger pinch  | Scroll down     |
| Open palm                   | Take screenshot |
 
Screenshots

![Screenshot (348)](https://github.com/user-attachments/assets/1a0abc70-7be8-4f94-b7b8-0da778f16c83)

Notes

* Use a well-lit environment for more accurate detection.
* The pinch threshold and detection confidence can be adjusted in the code for different hand sizes or camera qualities.

