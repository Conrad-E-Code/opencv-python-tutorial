import cv2
import random
img = cv2.imread('assets/truck.jpg', 1)

img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)

# for i in range(100):
#         for j in range(img.shape[1]):
#                 img[i][j] = [255, random.randint(0, 255), random.randint(0, 255)]

truckfront = img[180:320, 30:530]

img[0:140, 0:500] = truckfront
# 140 rows by 500 columns
# 180-319 h 
# 62-529 w
cv2.imshow("Truck", img)


cv2.waitKey(0000)
cv2.destroyAllWindows()