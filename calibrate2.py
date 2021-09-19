from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep

def leg1(angle1, angle2, angle3):
    kit.servo[0].angle = 180 - angle1
    kit.servo[1].angle = 180 - angle2
    kit.servo[2].angle = 180 - angle3

def leg2(angle1, angle2, angle3):
    kit.servo[3].angle = angle1
    kit.servo[4].angle = angle2
    kit.servo[5].angle = angle3

def leg3(angle1, angle2, angle3):
    kit.servo[6].angle = 180 - angle1
    kit.servo[7].angle = 180 - angle2
    kit.servo[8].angle = 180 - angle3

def leg4(angle1, angle2, angle3):
    kit.servo[9].angle = angle1
    kit.servo[10].angle = angle2
    kit.servo[11].angle = angle3

maxval = 50
minval = 180
stableval = 130

ldown = 40
lup = 120

sleeptime = 1

testno = 110

leg1(stableval, lup, lup)
leg2(stableval, lup, lup)
leg3(stableval, lup, lup)
leg4(stableval, lup, lup)

sleep(1)

leg1(stableval, ldown, ldown)
leg2(stableval, ldown, ldown)
leg3(stableval, ldown, ldown)
leg4(stableval, ldown, ldown)

#sleep(1)

#leg1(minval, lup, lup)
#leg2(minval, lup, lup)
#leg3(minval, lup, lup)
#leg4(minval, lup, lup)

#sleep(1)

#leg1(minval, ldown, ldown)
#leg2(minval, ldown, ldown)
#leg3(minval, ldown, ldown)
#leg4(minval, ldown, ldown)

#sleep(1)















