import numpy as np
import cv2
import urllib.request
#  Make sure camera stream is activated. WSL can't connect to webcm by default.

cap = cv2.VideoCapture()
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()