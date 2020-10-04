from gpiozero import Robot, DistanceSensor
from time import sleep
import uds
import random

left_echo_pin = 22
left_trigger_pin = 27
centre_echo_pin = 17
centre_trigger_pin = 4
right_echo_pin = 9
right_trigger_pin = 10

threshold = 18
threshold2 = 23
fast = 1
slow = 0.5

class robot():
    def __init__(self,robot):
        robot = self.robot
    def go_forwards(speed):
        robot.forward(speed)
        print("Going forwards")


    def go_backwards(speed):
        robot.backward(speed)
        print("Going backwards")


    def go_left(speed):
        robot.left(speed)
        print("Turning Left")


    def go_right(speed):
        robot.right(speed)
        print("Turning Right")

    def stop():
        robot.stop()
        print('stopping')

    def autonomous(dead_end):
        #take UDS readings
        print('running autonomous.py')
        left_distance = uds.calc_dist_cm(left_trigger_pin, left_echo_pin)
        centre_distance = uds.calc_dist_cm(centre_trigger_pin, centre_echo_pin)
        right_distance = uds.calc_dist_cm(right_trigger_pin, right_echo_pin)
        
        #print the results on the screen. Distance is in centimetres
        print(left_distance, centre_distance, right_distance)

        if left_distance < threshold and centre_distance > threshold and right_distance > threshold:
            go_right(fast)
        elif left_distance < threshold and centre_distance < threshold and right_distance > threshold:
            go_right(fast)
        
        elif left_distance > threshold and centre_distance > threshold and right_distance < threshold:
            go_left(fast)
        elif left_distance > threshold and centre_distance < threshold and right_distance < threshold:
            go_left(fast)

        elif left_distance < threshold2 and centre_distance < threshold2 and right_distance < threshold2:
            print('Dead End')
            dead_end += 1
            go_backwards(slow)
            sleep(0.1)
            if left_distance < right_distance :
                go_right(fast)
            else:
                go_left(fast)
            sleep(0.1)
            if left_distance < right_distance :
                go_right(fast)
            else:
                go_left(fast)
            sleep(0.1)


        elif left_distance > threshold and centre_distance < threshold and right_distance > threshold:
            if left_distance < right_distance:
                go_right(fast)
            else:
                go_left(fast)

        elif left_distance > threshold2 and centre_distance > threshold2 and right_distance > threshold2:
            go_forwards(fast)
            dead_end = 0

        elif left_distance < threshold2 or centre_distance < threshold2 or right_distance < threshold2:
            go_forwards(slow)

        if dead_end == 5:
            print("Can't get through - turning around!")
            if left_distance < right_distance :
                go_right(fast)
            else:
                go_left(fast)
            sleep(1)
            dead_end = 0


