import numpy as np
import cv2 as cv
print("CV2 version:", cv.__version__)

if __name__ == '__main__':
    cap = cv.VideoCapture(0) #select capture device, 0 is inbuild
    if not cap.isOpened():
        print("Can't find capture devide")
        exit(1) #Exit error code

#Face detection training set
face_cascade = cv.CascadeClassifier('haarcascade_profileface.xml')

print("press q to exit") #Refference to "#Display Frame" further down.

while True:
    #Capture frame by frame
    ret, frame = cap.read() #ret: obtain value from source. Frame: get next frame
    if (type(frame) == type(None)):
        break

    #Frame proccessing
    gray_color = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #BGR color scheme to GRAY color scheme

    ''' Optimization of image proccessing
    mini = cv.resize(frame, (frame.shape[1] // dst.size(), frame.shape[0] // dst.size()))
    '''
    #Detect objects of different sizes
    face_size = face_cascade.detectMultiScale(gray_color, 1.1, 1)

    #Create rectangle around detected objects
    for (x,y,w,h) in face_size: #x-axis, y-axis, wight, height
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        print("detect at:", x,y)

    #Display Frame
    cv.imshow('cap',frame) #Display
    if cv.waitKey(1) & 0xFF == ord('q'): #close by keypress q
        break #exit loop

cap.release() #release capture device
cv.destroyAllWindows() #Kill window
