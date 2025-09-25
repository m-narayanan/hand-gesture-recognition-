import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def get_finger_status(hand_landmarks):
    """
    Returns a dictionary of finger states: True if extended (Open), False if folded (Closed).
    Thumb is checked on x-axis, other fingers on y-axis.
    """
    finger_status = {}

    # Index–Pinky: check y-axis (tip above middle joint landmark (PIP) = extended)
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    for tip, pip in zip(tips, pips):
        finger_status[tip] = hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y

    # Thumb: check x-axis (tip left of joint for right hand)
    finger_status[4] = hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x

    return finger_status

def classify_gesture(finger_status):
    # Classifies gesture based on finger state
    thumb  = finger_status[4]
    index  = finger_status[8]
    middle = finger_status[12]
    ring   = finger_status[16]
    pinky  = finger_status[20]

    # 1) All extended
    if all([thumb, index, middle, ring, pinky]):
        return "Open Palm"

    # 2) All folded
    if not any([thumb, index, middle, ring, pinky]):
        return "Fist"

    # 3) Pointing: only index
    if index and not middle and not ring and not pinky and not thumb:
        return "Pointing"

    # 4) Rock On: index + pinky (+ thumb optional)
    if index and pinky and not middle and not ring:
        return "Rock On"

    # 5) Call Me: thumb + pinky only
    if pinky and thumb and not ring and not middle and not index:
        return "Call Me"

    # 6) Peace sign: index + middle only
    if index and middle and not ring and not pinky:
        return "Peace Sign"

    # 7) Thumbs up: thumb only
    if thumb and not any([index, middle, ring, pinky]):
        return "Thumbs Up"

    return "Unknown"

def main():
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as hands:

        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                continue

            # Flip for mirror imaege
            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape

            # Converting BGR to RGB
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            gesture_name = "No Hand Detected"

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Drawing landmarks
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Get finger states and classify
                    finger_status = get_finger_status(hand_landmarks)
                    gesture_name = classify_gesture(finger_status)

            # Overlay gesture name
            cv2.rectangle(frame, (10, 10), (300, 50), (0, 0, 0), -1)
            cv2.putText(frame, f"Gesture: {gesture_name}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            cv2.imshow("Hand Gesture Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
