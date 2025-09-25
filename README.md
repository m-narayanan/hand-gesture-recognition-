# Real-Time Hand Gesture Recognition

## Author
**Name:** Narayanan M  
---

## Objective
This project demonstrates real-time recognition of static hand gestures using a webcam. The goal is to detect a hand, extract its landmarks, and classify the pose into one of a predefined set of gestures.

---

## Technology Justification
For this project, I selected **MediaPipe Hands** and **OpenCV** as the core technologies.

**MediaPipe Hands** was chosen because it provides accurate, real-time hand landmark detection with minimal setup. It outputs 21 landmarks per hand, which is sufficient to classify static gestures without the need to train a custom model. This makes it efficient and reliable for the assignment’s requirements.

**OpenCV** was used to capture the webcam feed and display the results. It is a widely adopted library for computer vision tasks and integrates smoothly with MediaPipe. It also provides simple functions for drawing landmarks and overlaying text on video frames.

**Why not other methods?**  
- Training a deep learning model from scratch would require a dataset, more compute resources, and additional time. This was unnecessary since MediaPipe already provides robust hand tracking.  
- Traditional contour‑based methods (such as thresholding or convex hulls) are less reliable because they are sensitive to lighting and background changes.  
- MediaPipe offered the best balance of accuracy, speed, and ease of integration for this task.

---

## Gesture Logic Explanation
The gesture recognition logic is based on simple rules that check whether each finger is extended or folded.

- For the **index, middle, ring, and pinky fingers**, the tip landmark is compared with the proximal interphalangeal (PIP) joint landmark. If the tip is higher (smaller y‑coordinate) than the joint, the finger is considered extended. Otherwise, it is folded.  
- For the **thumb**, the tip landmark is compared with its joint on the x‑axis, since the thumb bends sideways. If the tip is positioned outward relative to the joint, the thumb is considered extended.

Using these rules, the following gestures are classified:

- **Open Palm**: All five fingers extended  
- **Fist**: All fingers folded  
- **Peace Sign**: Index and middle extended, others folded  
- **Thumbs Up**: Only the thumb extended, others folded  

I found it as this rule‑based approach is simple, explainable, and effective for static gesture recognition in real time.

---

## Project Structure
```
hand_gesture_recognition/
├── src/
│   ├── webcam_test.py         # Webcam test
│   ├── hand_detection.py      # Hand detection with landmarks
│   └── gesture_recognition.py # Full gesture recognition
│  
├── demo/
│   └── demo.mp4               # Screen recording of gestures
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## Setup and Execution Instructions

### 1. Clone the repository
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

## Demonstration
A short demo video (`demo/demo.mp4`) is included in the repository. It shows the application successfully identifying the four required gestures: Open Palm, Fist, Peace Sign, Thumbs Up etc.

---

## Dependencies
See `requirements.txt`:
```
opencv-python
mediapipe
numpy
```

---

## Credits
- MediaPipe Hands – for hand detection and landmarks  
- OpenCV – for video capture and visualization  

Would you like me to also prepare a **short checklist** (like a submission readiness list) so you can confirm everything is in place before you push to GitHub and email the link?
