import cv2
import mediapipe as mp
import pyautogui
import math
import numpy as np
import datetime

# Initialize Mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

# Capture video from webcam
cap = cv2.VideoCapture(0)

# Define gesture functions

def calculate_distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2 + (point1.z - point2.z)**2)


def is_index_finger_up(hand_landmarks):
    return hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y

def is_thumb_and_finger_pinch(hand_landmarks, finger_tip_index):
    thumb_tip = hand_landmarks.landmark[4]
    finger_tip = hand_landmarks.landmark[finger_tip_index]
    distance = calculate_distance(thumb_tip, finger_tip)
    return distance < 0.04  # Adjusted threshold for pinch detection



def is_open_palm(hand_landmarks):
    # Check if all fingers are up by comparing each finger tip's y-coordinate to the respective joint below it
    return (
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and  # Index finger
        hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y and  # Middle finger
        hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y and  # Ring finger
        hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y  # Pinky finger
    )



while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)
    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the RGB image
    results = hands.process(image_rgb)

    # Draw hand landmarks and implement gestures
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            

            if is_open_palm(hand_landmarks):
                screenshot = pyautogui.screenshot()
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                screenshot.save(f'screenshot_{timestamp}.png')
                print("Open palm detected, taking screenshot")

            # Move the cursor with the index finger
            if is_index_finger_up(hand_landmarks):
                # Get coordinates of index finger tip (landmark 8)
                index_finger_tip = hand_landmarks.landmark[8]
                x = int(index_finger_tip.x * screen_width)
                y = int(index_finger_tip.y * screen_height)
                # Move the mouse to the coordinates
                pyautogui.moveTo(x, y)

            # Detect pinch gestures for mouse actions
            if is_thumb_and_finger_pinch(hand_landmarks, 8):  # Thumb and index finger pinch
                print("Thumb and index finger pinch detected (Left Click)")
                pyautogui.click()
                cv2.putText(image, "Left Click", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            elif is_thumb_and_finger_pinch(hand_landmarks, 12):  # Thumb and middle finger pinch
                print("Thumb and middle finger pinch detected (Right Click)")
                pyautogui.click(button='right')
                cv2.putText(image, "Right Click", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            elif is_thumb_and_finger_pinch(hand_landmarks, 16):  # Thumb and ring finger pinch
                print("Thumb and ring finger pinch detected (Scroll Up)")
                pyautogui.scroll(10)
                cv2.putText(image, "Scroll Up", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            elif is_thumb_and_finger_pinch(hand_landmarks, 20):  # Thumb and pinky finger pinch
                print("Thumb and pinky finger pinch detected (Scroll Down)")
                pyautogui.scroll(-10)
                cv2.putText(image, "Scroll Down", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Virtual Mouse', image)

    if cv2.waitKey(5) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()