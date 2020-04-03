import numpy as np
import cv2
import pyautogui
import keyboard
import time

pyautogui.FAIL_SAFE = True
pyautogui.PAUSE = 1

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
hand_cascade = cv2.CascadeClassifier('hand.xml')

cap = cv2.VideoCapture(0)



while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    hands = hand_cascade.detectMultiScale(gray, 1.3, 10)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        if (y >= 180):           
            keyboard.press("shift")
        else:
            keyboard.release("shift")
        if (w >= 250):
            keyboard.press("w")
        else:
            keyboard.release("w")
        if (w <= 200):
            keyboard.press("s")
        else:
            keyboard.release("s")
        if (x <= 100):
            keyboard.press("d")
        else:
            keyboard.release("d")
        if (x >= 350):
            keyboard.press("a")
        else:
            keyboard.release("a")
        if (y <= 100):
            keyboard.press("space")
        else:
            keyboard.release("space")

    for (x, y, w, h) in hands:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0 ,255 ,100),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if (hands != ()):
            keyboard.press("ctrl")
        else:
            keyboard.release("ctrl")
    
        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
