import cv2
import mediapipe as mp
import time
import pyautogui as pg
import os
import threading
import math

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

pg.FAILSAFE = False

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

mpHand = mp.solutions.hands
hands = mpHand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

id_loc_dict = {}
pTime = 0

left_click_flag = True
right_click_flag = True
desktop_flag = True

prev_cursor_pos = None
cursor_sensitivity = 1.5

prev_scroll_y = None
scroll_history = []
scroll_sensitivity = 5

gesture_label = ""
os.system('cls')

print("[LOADING] Initializing camera and hand tracking...")
loading = True


def commands(command):
    global left_click_flag, right_click_flag, gesture_label
    if command == "left_click" and left_click_flag:
        pg.leftClick()
        gesture_label = "Click"
        print("clicked at", pg.position())

    elif command == "right_click" and right_click_flag:
        pg.rightClick()
        gesture_label = "Right Click"
        print("right clicked at", pg.position())

    elif command == "move":
        global prev_cursor_pos
        x1, y1 = id_loc_dict[8]
        x2, y2 = id_loc_dict[12]
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        if prev_cursor_pos is not None:
            dx = (mid_x - prev_cursor_pos[0]) * cursor_sensitivity
            dy = (mid_y - prev_cursor_pos[1]) * cursor_sensitivity
            pg.moveRel(dx, dy)
            gesture_label = "Move"
        prev_cursor_pos = (mid_x, mid_y)

    elif command == "scroll":
        global prev_scroll_y, scroll_history
        if 12 in id_loc_dict and 16 in id_loc_dict:
            y1 = id_loc_dict[12][1]
            y2 = id_loc_dict[16][1]
            scroll_mid_y = (y1 + y2) // 2
            if abs(id_loc_dict[12][0] - id_loc_dict[16][0]) < 60:
                if prev_scroll_y is not None:
                    dy = scroll_mid_y - prev_scroll_y
                    scroll_history.append(dy)
                    if len(scroll_history) > 3:
                        scroll_history.pop(0)
                    avg_dy = sum(scroll_history) / len(scroll_history)
                    if abs(avg_dy) > 2:
                        pg.scroll(-int(avg_dy / scroll_sensitivity))
                        gesture_label = "Scroll"
                prev_scroll_y = scroll_mid_y
            else:
                prev_scroll_y = None
                scroll_history = []

    elif command == "desktop" and desktop_flag:
        pg.hotkey("win", "d")
        gesture_label = "Desktop"

    elif command == "close":
        cam.release()
        cv2.destroyAllWindows()
        os.system('cls')
        print("closed")

id_title = {8: 'Left Click', 12: 'Right Click', 16: 'Desktop', 20: 'Close'}

while True:
    success, img = cam.read()
    img = cv2.flip(img, 1)
    try:
        img = cv2.resize(img, (1920, 1080))
    except:
        pass

    if loading:
        cv2.putText(img, "Loading Hand Tracking...", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)


    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    gesture_label = ""
    if results.multi_hand_landmarks:
        if loading:
            print("[READY] Hand tracking initialized.")
            loading = False

        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                id_loc_dict[id] = (cx, cy)
                if id in id_title:
                    cv2.putText(img, id_title[id], (cx+1, cy+1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 1)

            # Move
            if 8 in id_loc_dict and 12 in id_loc_dict and distance(id_loc_dict[8], id_loc_dict[12]) < 50:
                threading.Thread(target=commands, args=("move",)).start()

            # Scroll
            if 12 in id_loc_dict and 16 in id_loc_dict and distance(id_loc_dict[12], id_loc_dict[16]) < 50:
                threading.Thread(target=commands, args=("scroll",)).start()

            # Left Click
            if 4 in id_loc_dict and 8 in id_loc_dict and distance(id_loc_dict[4], id_loc_dict[8]) < 35:
                threading.Thread(target=commands, args=("left_click",)).start()
                left_click_flag = False
            else:
                left_click_flag = True

            # Right Click
            if 4 in id_loc_dict and 12 in id_loc_dict and distance(id_loc_dict[4], id_loc_dict[12]) < 35:
                threading.Thread(target=commands, args=("right_click",)).start()
                right_click_flag = False
            else:
                right_click_flag = True

            # Desktop
            if 4 in id_loc_dict and 16 in id_loc_dict and distance(id_loc_dict[4], id_loc_dict[16]) < 35:
                threading.Thread(target=commands, args=("desktop",)).start()
                desktop_flag = False
            else:
                desktop_flag = True

            # Close: fingertips close to their respective base joints (horizontal palm)
            if all(i in id_loc_dict for i in [5, 8, 9, 12, 13, 16, 17, 20]):
                if (distance(id_loc_dict[8], id_loc_dict[5]) < 25 and
                    distance(id_loc_dict[12], id_loc_dict[9]) < 25 and
                    distance(id_loc_dict[16], id_loc_dict[13]) < 25 and
                    distance(id_loc_dict[20], id_loc_dict[17]) < 25):
                    threading.Thread(target=commands, args=("close",)).start()

            mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)

    # Show FPS and Gesture Label
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)
    if gesture_label:
        cv2.putText(img, f"Gesture: {gesture_label}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()