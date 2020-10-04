#This program tests that you have the UDS GPIO mapping correct on your CERC Robot V2 chassis
#refer to GPIO pins allocations here: https://www.raspberrypi.org/documentation/usage/gpio/

# then import the 'sleep' class from the 'time' library (so we can add pauses in our program)
from time import sleep
import uds

left_echo_pin = 22
left_trigger_pin = 27
centre_echo_pin = 17
centre_trigger_pin = 4
right_echo_pin = 9
right_trigger_pin = 10


#begin looping forever
while True:
    
    #take a reading from the left, centre and right Ultra Sound Distance Sensors
    left_distance = uds.calc_dist_cm(left_trigger_pin, left_echo_pin)
    centre_distance = uds.calc_dist_cm(centre_trigger_pin, centre_echo_pin)
    right_distance = uds.calc_dist_cm(right_trigger_pin, right_echo_pin)

    # Print out the measurements
    print(left_distance, centre_distance, right_distance)

    #wait a second between each scan
    sleep(1)