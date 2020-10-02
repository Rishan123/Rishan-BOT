from gtts import gTTS
import os

tts = gTTS('hello')
tts.save('hello.mp3')
os.system('omxplayer /home/pi/Rishan-BOT/TTS/hello.mp3')
print('hello')