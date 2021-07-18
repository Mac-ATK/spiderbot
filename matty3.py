from adafruit_servokit import ServoKit
kit = ServoKit(channels=8)
from time import sleep

def leg1(angle1, angle2, angle3):
    kit.servo[0].angle = angle1
    kit.servo[1].angle = angle2
    kit.servo[2].angle = angle2

def leg2(angle1, angle2, angle3):
    kit.servo[3].angle = 180 - angle1
    kit.servo[4].angle = angle2
    kit.servo[5].angle = angle2

maxval = 10
minval = 170


leg1(maxval, 90, 90)
leg2(maxval, 90, 90)

sleep(2)

leg1(minval, 90, 90)
leg2(minval, 90, 90)

sleep(2)

leg1(maxval, 90, 90)
leg2(maxval, 90, 90)

sleep(2)

leg1(minval, 90, 90)
leg2(minval, 90, 90)









