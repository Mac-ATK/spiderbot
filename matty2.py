from adafruit_servokit import ServoKit
kit = ServoKit(channels=8)
from time import sleep

def leg1(angle1, angle2):
    kit.servo[0].angle = angle1
    kit.servo[1].angle = angle2



def smooth_jab(split):
    interval = 180 / split
    start = 0
    leg1(start, start)
    sleep(0.5)
    while start < 180:
        start = start + interval
        leg1(start, start)
        sleep(0.001)

smooth_jab(200)






