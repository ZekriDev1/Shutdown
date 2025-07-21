import cv2
import mediapipe as mp
import time
import os

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5)
cap = cv2.VideoCapture(1) #change The number with your camera Number mine are "1"

prev_x = None
wave_count = 0
wave_start_time = time.time()
cancel_shutdown = False

def shutdown():
    print("Shutting down in 3 seconds... Press 'C' to cancel.")
    for i in range(30):
        if cv2.waitKey(100) & 0xFF == ord('c'):
            print("Shutdown canceled.")
            return
    os.system("shutdown /s /t 1")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x

            if prev_x is not None:
                dx = x - prev_x
                if abs(dx) > 0.03:
                    wave_count += 1
                    print("Wave detected:", wave_count)
            prev_x = x

        if time.time() - wave_start_time > 3:
            if wave_count >= 4:
                cv2.putText(frame, "WAVE DETECTED - SHUTDOWN IN 3s", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow("Wave to Shutdown", frame)
                shutdown()
                break
            wave_count = 0
            wave_start_time = time.time()

    cv2.putText(frame, f"Wave Count: {wave_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Wave to Shutdown", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
