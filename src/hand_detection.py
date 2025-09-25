import cv2
import mediapipe as mp

def main():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils
    
    
    for id, lm in enumerate(hand_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.putText(frame, str(id), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip for natural feel (mirror effect)
        frame = cv2.flip(frame, 1)

        # Convert BGR to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Hand Detection with Landmark co-ordinates", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
