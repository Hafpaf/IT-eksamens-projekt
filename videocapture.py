import numpy as np
import cv2 as cv
print("CV2 version:", cv.__version__)

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if tuple(self.n) <= tuple(self.max):
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

'''class InfIter:
    """Infinite iterator to return all numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num'''

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
        #iter_list = int(iter(x))
        # end coords are the end of the bounding box x & y
        end_cord_x = x + w
        end_cord_y = y + h
        end_size = w*2

        # these are our target coordinates
        targ_cord_x = int((end_cord_x + x)/2)
        targ_cord_y = int((end_cord_y + y)/2)

        cv.rectangle(frame,(x,y),(end_cord_x,end_cord_y),(0,0,255),2) #print in red color
#        print("detection at:", "x:",x,"y:",y)
        coordtext = (str(x) + 'x' + ',' + str(y) + 'y')
        cv.putText(frame,coordtext,(0,30),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2) #print text on video

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


    #Display Frame
    cv.imshow('Face reconitization with Haar Cacades training set',frame) #Display
    if cv.waitKey(1) & 0xFF == ord('q'): #close by keypress q
        break #exit loop

cap.release() #release capture device
cv.destroyAllWindows() #Kill window
