# TacRead-Module-Testing-Application

When you run the modified module testing application 'RBD_modified.py' you can clearly see the added features. The original 'RB2.py' is also available in the 'RBD_test_code.zip' for comparison.
What has been added is that the modified app can detect an attached camera (other than webcam) using 'cam_check.py' and can start taking pictures at regular intervals or whenever you demand using 'check_camout.py' to process it to determine the pin condition (high or low).
The modified app can now output (in theory) the physical condition of braille pins in real time.
Different colour schemes have been added in GUI to indicaate different cases like: blue when actually pin is high but input was low; green when both the input and  outputs are the same etc
https://github.com/nimble00/PTGREY-cameras-with-python - This repository has the appropriate scripts that are required to interface with stereo cameras using python. This code is hardly available on internet and it took us a lot of time to succesfully communicate with the given PTGrey camera.
The github/useful/ has the appropriate files that are required to process the image to the point that we can easily and accurately(not actually) say what pins are high and which ones are low.
All these scripts run in parallel to deliver the asked specifications. Now all these scripts work with each other absolutely fine but the app fails to deliver the right output becacuse of the limitations of image processing in providing the exact knowledge of pin's condition (high or low), we also tried applying machine learning but it was still beyond our scope to succsesfully deliver the said requirements.
