# import the necessary packages
import pytesseract
import cv2
from gtts import gTTS
import os

# load the example image and convert it to grayscale
image = cv2.imread('/home/pi/Rishan-BOT/computer-vision/example_01.png')
config = ('-l eng --oem 1 --psm 3')

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.threshold(image, 0, 255,
    cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

text = pytesseract.image_to_string(image, config=config)
tts = gTTS(text)
tts.save('/home/pi/text.mp3')
os.system('omxplayer /home/pi/text.mp3')

print(text)
cv2.imshow('OCR',image)
cv2.waitKey(0)