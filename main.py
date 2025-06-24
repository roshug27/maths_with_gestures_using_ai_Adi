import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
import streamlit as st
import os
from PIL import Image

col1, col2 = st.columns([2,1])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    output_text_area = st.title("Answer")
    output_text_area = st.subheader("")
genai.configure(api_key="AIzaSyD036R7MgS66rRSUgIzAoyFOIIWemHiksg")

model = genai.GenerativeModel("gemini-1.5-flash")


cap = cv2.VideoCapture(0)
cap.set(propId= 3, value= 1280)
cap.set(propId= 4, value= 720)
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.8, minTrackCon=0.5)

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=True, flipType=True)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        print(fingers)
        return fingers,lmList
    else :
        return None


def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]
        if prev_pos is None: prev_pos = current_pos
        cv2.line(canvas, current_pos, prev_pos, (255, 0, 255), 10)
    elif fingers == [0,1,0,0,1]:
        canvas = np.zeros_like(img)
    return current_pos, canvas

def sendToAI(model,canvas,fingers):
    if fingers == [1,1,1,1,1]:
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["Solve This Math Problem.", pil_image])
        return response.text

prev_pos = None
canvas = None
image_combined = None
output_text= ""
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if canvas is None:
        canvas = np.zeros_like(img)
    info = getHandInfo(img)
    if info :
        fingers, lmList = info
        prev_pos, canvas = draw(info, prev_pos, canvas)
        output_text = sendToAI(model, canvas, fingers)
    image_combined = cv2.addWeighted(img, 0.6, canvas, 0.4, 0)
    FRAME_WINDOW.image(image_combined, channels="BGR")

    if output_text:
        output_text_area.text(output_text)
    # cv2.imshow("Image", img)
    # cv2.imshow("Canvas", canvas)
    # cv2.imshow("image_combined", image_combined)

    cv2.waitKey(1)