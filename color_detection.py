import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height= int(cap.get(4))

    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue= np.array([90,50,50])
    upper_blue= np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    # img = cv2.line(frame, (0,0), (width, height), (255,255,0), 5)
    # img = cv2.rectangle(img, (100,100), (200,200), (128, 128, 5))
    # img = cv2.circle(img, (299,299), 60, (0, 0, 255), -1)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # img = cv2.putText(img, "LEts go open CV", (200, height-10), font, 1, (0,0,0), 5, cv2.LINE_AA)
    cv2.imshow("frame", result )
    cv2.imshow("mask", mask )
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cap.destroyAllWindows()

# color picker
# BGR_color = np.array([[[255,0,0]]])
# create one by one image
# x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
# convert BGR to HSV

# Access pixel as HSV
# x[0][0]