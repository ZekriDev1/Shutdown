# ✋ Hand Gesture PC Shutdown

Control your computer using just your hand!  
This project uses a webcam and MediaPipe to detect a **closed fist gesture** and shuts down your PC automatically.

---

## 📸 Demo

https://www.tiktok.com/@zekri_dev/video/7529568175059389702

---

## 🧠 How It Works

- Uses **MediaPipe** for real-time hand tracking
- Detects a **closed fist (✊)** held for 2 seconds
- Executes a system shutdown command

---

## 🛠️ Requirements

- Python 3.7+
- Webcam
- Libraries:
  ```bash
  pip install opencv-python mediapipe
