import subprocess
from subprocess import Popen,PIPE
import pyspin
from pyspin import PySpin
import time
import Tkinter
import os

while (1):
    system = PySpin.System.GetInstance()
    cam_list = system.GetCameras()
    f = open(os.path.join(os.getcwd(),'camera.txt'), 'w')
    if(len(cam_list)>0):
    	f.write('Connected')
      	#print('Seial_Port_was_already_closed')
      	#ser.close()
    else:
      	f.write('Disconnected')  # python will convert \n to os.linesep
    f.close()
    del f
    del cam_list
    time.sleep(0.5)
