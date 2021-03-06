import numpy as np
import cv2 as cv
from datetime import date, time, datetime
#import picamera
'''
----------
TODO:
Create iterator to track changes in captured frames
transfer output to remote file system
----------
'''

print("CV2 version:", cv.__version__) #Print OpenCV version

'''
#Make sure the programs is run directly and not as library
'''
if __name__ == '__main__':
    #test video: 'media/david.webm'
    #Pi capture: picamera.capture()
    cap = cv.VideoCapture('media/david.webm') #select capture device, 0 is inbuild
    if not cap.isOpened():
        print("Can't find capture device")
        exit(1) #Exit error code

#Face detection training set
face_cascade = cv.CascadeClassifier('media/data/haarcascade_profileface.xml')

print("press q to exit") #Refference to "#Display Frame" further down.

#Used for iterator
old_x = [0]
old_y = [0]

current_date_time = datetime.now() #fetch current time
format = "%Y-%m-%d-%H:%M:%S" #specify formating of time and date
format_current = current_date_time.strftime(format) #format time and date

while True:
    #Capture frame by frame
    ret, frame = cap.read() #ret: obtain value from source. Frame: get next frame
    if (type(frame) == type(None)):
        break

    #Frame proccessing
    gray_color = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #BGR color scheme to GRAY color scheme

    #Detect objects of different sizes
    face_size = face_cascade.detectMultiScale(gray_color, 1.1, 1)

    '''
    ----------
    Convert detections to coordinates
    '''
    #Create rectangle around detected objects
    for (x,y,w,h) in face_size: #x-axis, y-axis, wight, height
        #iter_list = int(iter(x))
        # end coords are the end of the bounding box x & y
        end_cord_x = x + w
        end_cord_y = y + h
        end_size = w*2

        '''
        ----------
        #Write red square around detected face
        '''
        #Target coordinates
        targ_cord_x = int((end_cord_x + x)/2)
        targ_cord_y = int((end_cord_y + y)/2)

        cv.rectangle(frame,(x,y),(end_cord_x,end_cord_y),(0,0,255),2) #print in red color
        #print("detection at:", "x:",x,"y:",y) #Remain commented, use for tests
        coordtext = (str(x) + 'x' + ',' + str(y) + 'y')
        cv.putText(frame,coordtext,(0,30),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2) #print text on video

        '''
        ----------
        #write detections to file
        '''
        #print(format_current)
        current_date_time = datetime.now() #fetch current time
        format = "%Y-%m-%d-%H:%M:%S" #specify formating of time and date
        format_current_text = current_date_time.strftime(format) #format time and date
        with open('media/output/' + str(format_current) + '.txt', 'a') as f: #create file named after the current date and time
            f.write(' '.join((format_current_text + ': ' + coordtext,'\n'))) #write to file

        '''
        ----------
        #Write a circle unto the middle of detected faces
        '''
        for i in old_x:
            #x_iter = iter(old_x)
            #y_iter = iter(old_y)

            #cv.circle(frame,((x+w),(y+h)),(5),(0,255,0),2)
            cv.circle(frame, (targ_cord_x, targ_cord_y), 5, (0,255,0), 2)
            #cv.circle(frame,((old_x[i]), (old_y[i])),(x, y),(0,255,0),2)
            print("Circle center", targ_cord_x, targ_cord_y)
            print("Box coords: ""x:",x,"y:",y,"w:",w,"h:",h)
            #old_x == old_x.append(x)
            #old_y == old_y.append(y)
            #print(i, old_x[i+1])
            #next(old_x)
            break

    '''
    ----------
    #Display Frame
    '''
    cv.imshow('Face reconitization with Haar Cacades training set',frame) #Display window with stated title
    if cv.waitKey(1) & 0xFF == ord('q'): #close by keypress q
        break #exit loop

#Kill process
cap.release() #release capture device
cv.destroyAllWindows() #Kill window
