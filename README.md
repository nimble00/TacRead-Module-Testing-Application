# TacRead-Module-Testing-Application
#  
1. When you run the modified module testing application 'RBD_modified.py' you can clearly see the added features. The original 'RB2.py' is also available in the 'RBD_test_code.zip' for comparison.
#
2. What has been added is that the modified app can detect an attached camera (other than webcam) using 'cam_check.py' and can start taking pictures at regular intervals or whenever you demand using 'check_camout.py' to process it and determine the pin condition (high or low), compare it with the given input and publish the results in real time.
# 
3. The modified app can now output (in theory) the physical condition of braille pins in real time, the user has been given the option to turn visual verfication on or off.
# 
4. Different colour schemes have been added in GUI to indicate different cases like: blue when actually pin is high but input was low; green when both the input and  outputs are the same etc
# 
5. https://github.com/nimble00/PTGREY-cameras-with-python - This repository has the appropriate scripts that are required to interface with stereo cameras using python. This code is hardly available on internet and it took us a lot of time to succesfully communicate with the given PTGrey camera.
# 
6. The github/useful/ has the appropriate files that are required to process the image to the point that we can easily and accurately(not actually) say what pins are high and which ones are low.
#  
7. All these scripts run in parallel to deliver the asked specifications. All these scripts work with each other absolutely fine but at the end of the day, the app fails to deliver the right output becacuse of the limitations of image processing in providing the exact knowledge of pin's condition (high or low).
#
8. We also tried applying machine learning but we couldn't develop enough expertise in the time left and because of that it was still beyond our scope to succsesfully deliver the said requirements.
