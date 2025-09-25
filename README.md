# Real-Time Hand Gesture Recognition

## What This Project Does
This project uses a webcam to recognize a few simple hand gestures in real time.  
Think of it like teaching your computer to read your hand signs.  

The app can spot:
- **Open Palm**  
- **Fist**  
- **Peace Sign**  
- **Thumbs Up**  
- **Pointing**
- **Rock On**
- **Call Me**

---

## Methodology 

Instead of training a heavy model, I leaned on **MediaPipe Hands**. It already gives you 21 hand landmarks. From there, I wrote simple rules to decide if a finger is open or closed.  

---

## Tools I Used
- **Python 3.9+** – the language of choice.  
- **OpenCV** – to grab webcam frames and draw on them.  
- **MediaPipe Hands** – to detect the hand and its landmarks.  
- **NumPy** – for quick math when needed.  

Why MediaPipe? Because it’s fast, accurate, and works out of the box. No need to reinvent the wheel.  

---

## How It Works
Here’s the flow:
1. OpenCV captures video from your webcam.  
2. MediaPipe finds your hand and marks 21 key points.  
3. A small set of rules checks which fingers are extended.  
4. Based on that, the app labels the gesture.  
5. The result shows up right on the video feed.  

Simple. Direct. Easy to explain.  

---

## Project Structure
```
hand_gesture_recognition/
├── src/
│   ├── webcam_test.py        # Just tests the webcam
│   ├── hand_detection.py     # Runs MediaPipe hand detection
│   └── gesture_recognition.py # Full gesture recognition
├── demo/                     # Demo video or gif
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

---

## How To Run It

### 1. Clone the repo
```bash
git clone <your-repo-link>
cd hand_gesture_recognition
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the scripts
- Test webcam:  
  ```bash
  python src/webcam_test.py
  ```
- Hand detection only:  
  ```bash
  python src/hand_detection.py
  ```
- Full gesture recognition:  
  ```bash
  python src/gesture_recognition.py
  ```

Press **q** to quit the window.  

---

## Demo
Check the `demo/` folder for a short video showing the gestures in action.  

---

## Future Ideas
- Add more gestures.  
- Support both hands at once.  
- Try dynamic gestures (like waving).  

---

## Credits
- MediaPipe Hands – official docs and examples.  
- OpenCV – for video and drawing.  

