from gpiozero import Robot
from time import sleep

robot = Robot(left=(18,3), right=(15,14))

robot.forward(speed=0.4)
sleep(1)
robot.stop()