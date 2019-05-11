# import the necessary packages
#import argparse
import cv2
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
		cv2.imshow("Camera View, Press 'r' to refresh & 'c' to exit.", image)
        #cv2.waitKey(0)

'''
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
'''
cap = cv2.VideoCapture(0)
ret,frame=cap.read()
# load the image, clone it, and setup the mouse callback function
#image = cv2.imread(args["image"])
image =  frame
#clone = image.copy()
cv2.namedWindow("Camera View, Press 'r' to refresh & 'c' to exit.")
cv2.setMouseCallback("Camera View, Press 'r' to refresh & 'c' to exit.", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("Camera View, Press 'r' to refresh & 'c' to exit.", image)
	key = cv2.waitKey(1) & 0xFF

	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		#image = clone.copy()
		r,fr=cap.read()
		image =  fr
		cv2.imwrite('prime.jpg',image)
	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break
def hi_lo():
	global refPt
	frame = cv2.imread('prime.jpg')
	print refPt
	#cv2.imshow("hkj.jpg",frame[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]])
	cv2.waitKey(0)

	ten = []
    #Slice current frame(photo) in 10 equal parts (vertically)
	for i in range(0,(refPt[1][0]-refPt[0][0]),abs(refPt[1][0]-refPt[0][0])//20):
		#tenvs.append(frame[i:i+(FRAME_WIDTH//10),FRAME_HEIGHT-FRAME_WIDTH/5:,:]) #finally (pins at top)
		ten.append(frame[refPt[0][1]:refPt[1][1],  refPt[0][0]+i: refPt[0][0]+i+abs(refPt[1][0]-refPt[0][0])//20]) #only for now (pins at bottom)
	for hj in range(20):
		cv2.imshow("hkj.jpg",ten[hj])
		cv2.waitKey(0)
# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
	roi = fr[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imshow("Bounding Box", roi)

	'''print refPt
	print refPt[0][1]'''
	cv2.waitKey(0)
	hi_lo()

# close all open windows
cv2.destroyAllWindows()
