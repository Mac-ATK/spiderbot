from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep

def leg1(angle1, angle2, angle3):
    kit.servo[0].angle = angle1
    kit.servo[1].angle = angle2
    kit.servo[2].angle = angle2

def leg2(angle1, angle2, angle3):
    kit.servo[3].angle = 180 - angle1
    kit.servo[4].angle = 180 - angle2
    kit.servo[5].angle = 180 - angle2

def leg3(angle1, angle2, angle3):
    kit.servo[6].angle = 180 - angle1
    kit.servo[7].angle = 180 - angle2
    kit.servo[8].angle = 180 - angle2

def leg4(angle1, angle2, angle3):
    kit.servo[9].angle = angle1
    kit.servo[10].angle = angle2
    kit.servo[11].angle = angle2

maxval = 50
minval = 180

ldown = 0
lup = 180

sleeptime = 1

testno = 110

leg1(minval, lup, lup)
leg2(minval, lup, lup)
leg3(minval, lup, lup)
leg4(minval, lup, lup)
















