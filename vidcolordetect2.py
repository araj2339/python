import numpy as np
import cv2

cap = cv2.VideoCapture(0)

boundaries = [([17, 15, 100], [50, 56, 200])]
#red

while (True):
    ret, frame = cap.read()
    for (lower,upper) in boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        mask = cv2.inRange(frame, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("frame", output)

    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()
