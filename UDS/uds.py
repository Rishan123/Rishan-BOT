from gpiozero import InputDevice, OutputDevice
import RPi.GPIO as GPIO
from time import sleep, time

def get_pulse_time(trig_pin, echo_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)
    cnt1 = 0
    cnt2 = 0

    GPIO.output(trig_pin, True)
    sleep(0.00001)
    GPIO.output(trig_pin, False)

    start = time()
    while GPIO.input(echo_pin) == 0:
        start = time()
        cnt1 += 1
        if cnt1 > 1000:
            break

    stop = time()
    while GPIO.input(echo_pin) == 1:
        stop = time()
        cnt2 += 1
        if cnt2 > 1000:
            break

    return (stop - start)

def calculate_distance(duration):
    speed = 343
    distance = speed * duration / 2
    return distance
    
def calc_dist_cm(trig_pin, echo_pin):
    duration = get_pulse_time(trig_pin, echo_pin)
    distance = calculate_distance(duration)
    distance_cm = distance*100
    dis_cm = int(distance_cm)
    # If the measured distance is greater than 70cm, then set the distance to 70cm.  
    # Otherwise the measurement is noisy and it can make the robot make incorrect decisions on which way to turn.
    if dis_cm > 70:
        dis_cm = 70
    #print(dis_cm, 'cm')  << Have removed this as the distance is reported in the main program
    return dis_cm
