# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     ret,frame = cap.read()
#     width = int(cap.get(3))
#     height= int(cap.get(4))

#     gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     corners = cv2.goodFeaturesToTrack(gray, 12, 0.1, 50)
#     corners = np.int0(corners)

#     for corner in corners:
#         x, y = corner.ravel()
#         cv2.circle(frame, (x, y), 20, (255,0,0), -1 )

#     for i in range(len(corners)):
#         for j in range( i+1, len(corners)):
#             corner1 = tuple(corners[i][0])
#             corner2 = tuple(corners[j][0])
#             color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
#             cv2.line(frame, corner1, corner2, color, 1)


#     cv2.imshow("frame", frame )

#     if cv2.waitKey(10) == ord('q'):
#         break
# cap.release()
# cap.destroyAllWindows()
# import numpy as np
# import cv2
# from scipy.spatial import cKDTree

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     width = int(cap.get(3))
#     height = int(cap.get(4))

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     corners = cv2.goodFeaturesToTrack(gray, 64, 0.2, 50)
#     corners = np.int0(corners)

#     # Create a KDTree using scipy
#     kdtree = cKDTree(corners[:, 0, :])

#     for i in range(len(corners)):
#         x, y = corners[i][0]

#         # Find the indices of the 3 nearest neighbors
#         _, indices = kdtree.query((x, y), k=4)

#         # Connect each corner to its three nearest neighbors
#         for j in indices[1:]:
#             neighbor = tuple(corners[j][0])
#             color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
#             cv2.line(frame, (x, y), neighbor, color, 1)

#     cv2.imshow("frame", frame)

#     if cv2.waitKey(10) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import numpy as np
# import cv2
# from scipy.spatial import cKDTree

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     width = int(cap.get(3))
#     height = int(cap.get(4))

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     corners = cv2.goodFeaturesToTrack(gray, 12, 0.1, 50)

#     if corners is not None and len(corners) >= 4:
#         corners = np.int0(corners)

#         # Create a KDTree using scipy
#         kdtree = cKDTree(corners[:, 0, :])

#         for i in range(len(corners)):
#             x, y = corners[i][0]

#             # Find the indices of the 3 nearest neighbors
#             _, indices = kdtree.query((x, y), k=4)

#             # Connect each corner to its three nearest neighbors
#             for j in indices[1:]:
#                 if j < len(corners):  # Check if the index is within bounds
#                     neighbor = tuple(corners[j][0])
#                     color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
#                     cv2.line(frame, (x, y), neighbor, color, 1)

#         cv2.imshow("frame", frame)

#     if cv2.waitKey(10) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


import numpy as np
import cv2
from scipy.spatial import cKDTree

cap = cv2.VideoCapture(0)

background = None

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, 12, 0.3, 50)

    if corners is not None:
        corners = np.int0(corners)

        # Store the current frame as the background
        background = frame.copy()

        # Create a KDTree using scipy
        kdtree = cKDTree(corners[:, 0, :])

        for i in range(len(corners)):
            x, y = corners[i][0]

            # Find the indices of the 3 nearest neighbors
            _, indices = kdtree.query((x, y), k=4)

            # Connect each corner to its three nearest neighbors
            for j in indices[1:]:
                if j < len(corners):  # Check if the index is within bounds
                    neighbor = tuple(corners[j][0])
                    color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
                    cv2.line(frame, (x, y), neighbor, color, 1)

        cv2.imshow("frame", frame)

    elif background is not None:
        # If no corners are detected, use the stored background
        frame = background.copy()
        cv2.imshow("frame", frame)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
