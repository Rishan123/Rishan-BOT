from gpiozero import Robot
from time import sleep

robot = Robot(left=(18,3), right=(15,14))
speed = 0.4

robot.forward(speed=speed)
sleep(1)
robot.backward(speed=speed)
sleep(1)
robot.left()
sleep(1)
robot.right()
sleep(1)
robot.stop()