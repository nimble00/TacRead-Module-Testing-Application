# import the necessary packages
import pyspin
from pyspin import PySpin
import pyflycapture2
#import argparse
import cv2
import numpy as np
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
global refPt
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("Camera View, Press 'r' to refresh & 'c' to exit.", np.asarray(np.asmatrix(image)))
        #cv2.waitKey(0)

'''
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
'''

system = PySpin.System.GetInstance()
cam_list = system.GetCameras()
if(cam_list>0):
    cam = cam_list.GetByIndex(0)
    # Initialize camera
    cam.Init()
    cam.AcquisitionMode.SetValue(PySpin.AcquisitionMode_SingleFrame)
    cam.BeginAcquisition()
    #k=np.array(image_primary)

#cap = cv2.VideoCapture(0)
#ret,frame=cap.read()

image = cam.GetNextImage()
print "1"
# load the image, clone it, and setup the mouse callback function
#image = cv2.imread(args["image"])
image = pyflycapture2.convert(image)
cv2.namedWindow("Camera View, Press 'r' to refresh & 'c' to exit.")
cv2.setMouseCallback("Camera View, Press 'r' to refresh & 'c' to exit.", click_and_crop)

print "2"
# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
    print "3"
    print cv_image
    cv2.imshow("Camera View, Press 'r' to refresh & 'c' to exit.", cv_image)
    print "4"
    key = cv2.waitKey(1) & 0xFF
    if key == ord("r"):
		image = cam.GetNextImage()
		row_bytes = float(len(image.getData()))/float(image.getRows())
		cv_image = np.array(image.getData(),dtype="uint8").reshape((image.getrows(),image.getCols()))
		cv2.imwrite('frame',cv_image)
    elif key == ord("c"):
		break
def hi_lo():
    global refPt
    frame = cv2.imread('prime.jpg')
    print refPt
    cv2.waitKey(0)
    ten = []
    for i in range(0,(refPt[1][0]-refPt[0][0]),abs(refPt[1][0]-refPt[0][0])//20):
        ten.append(frame[refPt[0][1]:refPt[1][1],  refPt[0][0]+i: refPt[0][0]+i+abs(refPt[1][0]-refPt[0][0])//20])
    for hj in range(20):
        cv2.imshow("hkj.jpg",ten[hj])
        cv2.waitKey(0)
if len(refPt) == 2:
    roi = fr[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    print "5"
    cv2.imshow("Bounding Box", roi)
    cv2.waitKey(0)
    hi_lo()
cv2.destroyAllWindows()
