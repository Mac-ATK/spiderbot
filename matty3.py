from adafruit_servokit import ServoKit
kit = ServoKit(channels=8)
from time import sleep

def leg1(angle1, angle2, angle3):
    kit.servo[0].angle = angle1
    kit.servo[1].angle = angle2
    kit.servo[2].angle = angle2

def leg2(angle1, angle2, angle3):
    kit.servo[3].angle = angle1
    kit.servo[4].angle = angle2
    kit.servo[5].angle = angle2


leg1(90, 90, 90)
leg2(90, 90, 90)









