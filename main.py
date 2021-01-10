# Helmet Detection Script

import sys
sys.path.append('/usr/local/lib/python3.4/site-packages')

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import argparse

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image - this array
    # will be 3D, representing the width, height, and # of channels
    image = frame.array
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier('Path_to_XML_Classifier')
    
    faceRects=faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(30,30))
    for (fX,fY,fW,fH) in faceRects:
        cv2.rectangle(image,(fX,fY),(fX+fW,fY+fH),(0,255,0),2)
        # show the frame
        cv2.imshow("Frame",image)
        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
            
            