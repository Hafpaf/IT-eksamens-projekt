import numpy as np
import cv2 as cv
print("CV2 version:", cv.__version__)

if __name__ == '__main__':
    cap = cv.VideoCapture(0) #select capture device, 0 is inbuild
    if not cap.isOpened():
        print("Can't find capture devide")
        exit(1) #Exit error code

#Face detection training set
face_cascade = cv.CascadeClassifier('/media/data/haarcascade_profileface.xml')

print("press q to exit")
while True:
    #Capture frame by frame
    ret, frame = cap.read() #ret: obtain value from source. Frame: get next frame

    #Frame proccessing
    gray_color = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #BGR color scheme to GRAY color scheme

    #Detect objects of different sizes
    face_size = face_cascade.detectMultiScale(gray_color, 1.1, 1)

    #Create rectangle around detected objects
    for (x,y,w,h) in face_size:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    #Display Frame
    cv.imshow('frame',gray) #Display
    if cv.waitKey(1) & 0xFF == ord('q'): #close by keypress q
        break #exit loop

cap.release() #release capture device
cv.destroyAllWindows() #Kill window
