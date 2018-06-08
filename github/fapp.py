import cv2
import cv
import numpy as np
from operator import itemgetter

'''
im =  cv2.imread("fou2.jpg")
#im = cv2.resize(im,(640,512))
smallest = np.amin(im)
biggest = np.amax(im)
print smallest
print " "
print biggest
cv2.imwrite("asas.jpg",im)
'''

global frame
global FRAME_WIDTH
global FRAME_HEIGHT

def newframe():
    #started the Capture
    cap = cv2.VideoCapture(0)
    #check if 'cap' actually started
    if cap.isOpened():
        #Capture frame-by-frame: frame => current capture & ret => true or false
        ret, frame = cap.read()

    FRAME_WIDTH = cv2.VideoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    FRAME_HEIGHT = cv2.VideoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)

#function returns the pins' condition
def hi_lo(frame):
    ten = []
    #Slice current frame(photo) in 10 equal parts (vertically)
    for i in range(FRAME_WIDTH):
        #tenvs.append(frame[i:i+(FRAME_WIDTH//10),FRAME_HEIGHT-FRAME_WIDTH/5:,:]) #finally (pins at top)
        ten.append(frame[i:i+(FRAME_WIDTH//10),:FRAME_WIDTH/5,:]) #only for now (pins at bottom)

    cir = []
    #detecting circles in each of the sliced part
    for j in range(10):
        img = ten[j]
        img = cv2.medianBlur(img,7)
        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

        #making an array of detected circles' centers & radii => circles
        circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,20,
                                    param1=50,param2=5,minRadius=0,maxRadius=12)

        #rounding off all the numbers in the array 'circles'
        circles = np.uint16(np.around(circles))

        '''#drawing all circles' perimeters & centers (only for debugging purposes, not required finally)
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)

            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        '''

        #adding the circles in each slice to array 'cir'
        cir.append(circles[0])
        #for loop ends

    scir = []
    #sorted circles
    for k in range(10):
        newc = []
        new1 = []
        new2 = []
        tempa = sorted(cir[0], key=itemgetter(0))
        divv = (tempa[3][0]+ tempa[4][0])/2
        for l in range(8):
            if tempa[l][0] < divv:
                new1.append(tempa[l])
            else:
                new2.append(tempa[l])
        new1 = sorted(new1, key = itemgetter(1))
        new2 = sorted(new2, key = itemgetter(1))
        newc.append(new1)
        newc.append(new2)
        scir.append(newc)

    retarray = []
    for m in range(10):
        str = ""
        ta1 = scir[m][0][:-1]
        ta2 = scir[m][1][:-1]
        for v in ta1:
            if ten[m][v[0],v[1]] > 200:
                str = str+"1"
            else:
                str = str+"0"
        for w in ta2:
            if ten[m][w[0],w[1]] > 200:
                str = str+"1"
            else:
                str = str+"0"
        if ten[m][scir[m][0][-1][0],scir[m][0][-1][1]] > 200:
            str = str + "1"
        else:
            str = str+"0"

        if ten[m][scir[m][1][-1][0],scir[m][1][-1][1]] > 200:
            str = str + "1"
        else:
            str = str+"0"
        retarray.append(str)
    return retarray
    #function 'hi_lo' ends

    '''
        iarr = np.asarray(img, dtype="int32")

        print len(circles)
        print circles
        print iarr[70,724]
    '''


'''#waitkey(n) waits for keystroke for 'n' seconds; 0xFF = 11111111; ord('q') can return a random number
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
'''


'''
CV_CAP_PROP_FPS Frame rate.
'''


'''
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''

if __name__ == '__main__':
    raw_in = raw_input("Enter 's' to start testing or 'r' to cancel:":)
    if raw_in == 's':
        newframe()
        hi_lo(frame)
