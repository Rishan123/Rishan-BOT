# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from gtts import gTTS

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
config = ('-l eng --oem 1 --psm 3')
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    text = pytesseract.image_to_string(image, config=config)
    for i in text:
        if i in chars:
            print(text)
            tts = gTTS(text)
            tts.save('/home/pi/text.mp3')
            os.system('omxplayer /home/pi/text.mp3')
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

