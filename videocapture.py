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
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #BGR color scheme to GRAY color scheme


    face_gray = face_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,z,h) in face_gray:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    #Display Frame
    cv.imshow('frame',gray) #Display
    if cv.waitKey(1) & 0xFF == ord('q'): #close by keypress q
        break #exit loop

cap.release()
cv.destroyAllWindows()
