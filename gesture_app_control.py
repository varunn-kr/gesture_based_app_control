import cv2
import mediapipe as mp
import time
import os
import math
import pyautogui
from collections import deque


IP_CAMERA_URL = "http://192.168.1.5:8080/video"  
GESTURE_DELAY = 2.5        
SMOOTHING_FRAMES = 7       
MIN_HAND_SIZE = 0.08       


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(IP_CAMERA_URL)

last_action_time = 0
history = deque(maxlen=SMOOTHING_FRAMES)


def angle(a, b, c):
    ab = (a.x - b.x, a.y - b.y)
    cb = (c.x - b.x, c.y - b.y)
    dot = ab[0]*cb[0] + ab[1]*cb[1]
    mag = math.hypot(*ab) * math.hypot(*cb)
    if mag == 0:
        return 0
    return math.degrees(math.acos(dot / mag))

def is_finger_open(lm, tip, pip, mcp):
    return angle(lm[tip], lm[pip], lm[mcp]) > 160


def count_fingers(lm):
    fingers = [
        is_finger_open(lm, 8, 6, 5),    
        is_finger_open(lm, 12, 10, 9),  
        is_finger_open(lm, 16, 14, 13), 
        is_finger_open(lm, 20, 18, 17)  
    ]
    return sum(fingers)


def open_app(fingers):
    global last_action_time

    if time.time() - last_action_time < GESTURE_DELAY:
        return

    if fingers == 1:
        os.system("start https://www.youtube.com")
        print("Opened YouTube")

    elif fingers == 2:
        os.system("start https://music.youtube.com")
        print("Opened YouTube Music")

    elif fingers == 3:
        os.system("start brave")
        print("Opened Brave Browser")

    elif fingers == 0:
        pyautogui.hotkey("alt", "f4")
        print("Closed Active Window")

    else:
        return

    last_action_time = time.time()


while True:
    success, frame = cap.read()
    if not success:
        print("IP Camera not responding")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            
            hand_size = abs(lm[0].y - lm[9].y)
            if hand_size < MIN_HAND_SIZE:
                continue

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            count = count_fingers(lm)
            history.append(count)

            
            stable_count = max(set(history), key=history.count)
            open_app(stable_count)

            cv2.putText(
                frame,
                f"Fingers: {stable_count}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    cv2.imshow("Hand Gesture App Controller", frame)

    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()

