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
hipout = 120

ldown = 100
lup = 180

hipdiff = hipin - hipout

current_1 = hipin
current_2 = hipin
current_3 = hipin-(hipdiff/3)
current_4 = hipin-(hipdiff/3)

leg1(current_1, lup, lup)
leg2(current_2, lup, lup)
leg3(current_3, lup, lup)
leg4(current_4, lup, lup)

for i in range(8):
    current_1 -= (hipdiff/3)
    current_2 -= (hipdiff/3)
    current_3 -= (hipdiff/3)
    current_4 -= (hipdiff/3)
    leg1(current_1, lup, lup)
    leg2(current_2, lup, lup)
    leg3(current_3, lup, lup)
    leg4(current_4, lup, lup)
    if current_1 == hipout:
        current_1 = hipin
        leg1(current_1, lup, lup)
    if current_2 == hipout:
        current_2 = hipin
        leg2(current_2, lup, lup)
    if current_3 == hipout:
        current_3 = hipin
        leg3(current_3, lup, lup)
    if current_4 == hipout:
        current_4 = hipin
        leg4(current_4, lup, lup)
    sleep(0.2)


















