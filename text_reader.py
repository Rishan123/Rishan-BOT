# import the necessary packages
from PIL import Image
import pytesseract
import os
import time
import cv2
from gtts import gTTS

def text_reader(frame):
    config = ('-l eng --oem 1 --psm 3')
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

    text = pytesseract.image_to_string(frame, config=config)

    return text

