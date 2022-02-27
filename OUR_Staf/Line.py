import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(-1)


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame[240:440, 150:489], cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", gray)

    if cv2.waitKey(1) == ord('q'):
       break