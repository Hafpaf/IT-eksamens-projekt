import numpy as np
import cv2 as cv
print("CV2 version:", cv.__version__)

if __name__ == '__main__':
    cap = cv.VideoCapture('media/david.webm') #select capture device, 0 is inbuild
    if not cap.isOpened():
        print("Can't find capture devide")
        exit(1) #Exit error code

#Face detection training set
face_cascade = cv.CascadeClassifier('media/data/haarcascade_profileface.xml')

print("press q to exit") #Refference to "#Display Frame" further down.

old_x = [0]
old_y = [0]


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
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2) #print in red color
#        print("detection at:", "x:",x,"y:",y)

    for (x,y,w,h) in face_size:
        #old_y = next(a)
        for i in old_x:
            cv.line(frame,((old_x[i]), (old_y[i])),(x, y),(0,255,0),2)
            print("x:",x,"y:",y,"w:",w,"h:",h)
            old_x == old_x.append(x)
            old_y == old_y.append(y)
            #i =+ 1
            break

    #Display Frame
    cv.imshow('Face reconitization with Haar Cacades training set',frame) #Display
    if cv.waitKey(1) & 0xFF == ord('q'): #close by keypress q
        break #exit loop

cap.release() #release capture device
cv.destroyAllWindows() #Kill window
