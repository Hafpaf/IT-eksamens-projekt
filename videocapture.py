import numpy as np
import cv2 as cv
print("CV2 version:", cv.__version__)

cap = cv.VideoCapture(0) #select capture device, 0 is inbuild

while True:
    #Capture frame by frame
    ret, frame = cap.read()

    #Frame proccessing
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #BGR color scheme to GRAY color scheme

    #Display Frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
