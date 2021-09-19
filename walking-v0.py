from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep
import threading

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

hipin = 180
hipout = 110

ldown = 0
lup = 180

leg1(hipin, lup, lup)

for i in range(8):
    diff = hipin - hipout
    current = hipin
    for i in range(4):
        current = current-(diff/4)
        leg1(current, lup, lup)
        sleep(0.5)
    current = hipout
    for i in range(4):
        current = current+(diff/4)
        leg1(current, lup, lup)
        sleep(0.5) 

















