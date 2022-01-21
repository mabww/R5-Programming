import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
while True:
    #capture frame-by-frame
    ret, frame = cap.read()
    #Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
#When done, release the capture
cap.release()
cv.destroyAllWindows()
