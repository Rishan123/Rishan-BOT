from gpiozero import Robot
from time import sleep

robot = Robot(left=(18,3), right=(15,14))
speed = 0.6

robot.forward(speed=speed)
sleep(1)
robot.backward(speed=speed)
sleep(1)
robot.left(speed=speed)
sleep(1)
robot.right(speed=speed)
sleep(1)
robot.stop()