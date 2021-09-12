from adafruit_servokit import ServoKit
kit = ServoKit(channels=8)
from time import sleep

def leg1(angle1, angle2, angle3):
    kit.servo[0].angle = 180 - angle1
    kit.servo[1].angle = 180 - angle2
    kit.servo[2].angle = 180 - angle3

def leg2(angle1, angle2, angle3):
    kit.servo[3].angle = angle1
    kit.servo[4].angle = angle2
    kit.servo[5].angle = angle3

maxval = 50
minval = 170

ldown = 0
lup = 180

sleeptime = 1


leg1(maxval, ldown, ldown)
leg2(maxval, ldown, ldown)

sleep(sleeptime)

leg1(minval, lup, lup)
leg2(minval, lup, lup)

sleep(sleeptime)

leg1(maxval, ldown, ldown)
leg2(maxval, ldown, ldown)

sleep(sleeptime)

leg1(minval, lup, lup)
leg2(minval, lup, lup)

sleep(sleeptime)











