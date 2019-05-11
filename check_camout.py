import subprocess
from subprocess import Popen,PIPE
import pyspin
from pyspin import PySpin
import time
import Tkinter
import cv2
import numpy as np
import os
DIR = os.getcwd()
while(1):
	system = PySpin.System.GetInstance()
	cam_list = system.GetCameras()
	if(cam_list>0):
		cam = cam_list.GetByIndex(0)
		# Initialize camera
		cam.Init()
		cam.AcquisitionMode.SetValue(PySpin.AcquisitionMode_SingleFrame)
		cam.BeginAcquisition()
		image_primary = cam.GetNextImage()
		#k=np.array(image_primary)


		image_primary.Save('primea.jpg')
		img = cv2.imread('primea.jpg',0)

		# create a CLAHE object (Arguments are optional).
		clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
		cl1 = clahe.apply(img)

		cv2.imwrite('prime.jpg',cl1)

		# Stop acquisition
		cam.EndAcquisition()

		# De-initialize
		cam.DeInit()

		# Clear references to images and cameras
		del image_primary
		del cam
		del cam_list
		    	# code for the file
