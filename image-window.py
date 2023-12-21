import cv2

img = cv2.imread('assets/truck.jpg', 0)
# 0 grayscale, -1 no transparancy, 1 unchanged color
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
img = cv2.rotate(img, cv2.ROTATE_180)
# cv2.imwrite("new_truck.jpg", img)
cv2.imshow("Truck", img)


cv2.waitKey(20000)
cv2.destroyAllWindows