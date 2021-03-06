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
hipout = 90

ldown = 90
lup = 180

hipdiff = hipin - hipout

current_1 = hipin
current_2 = hipin
current_3 = hipin-((hipdiff/3)*2)
current_4 = hipin-((hipdiff/3)*2)

leg_1 = ldown
leg_2 = ldown
leg_3 = ldown
leg_4 = ldown

leg1(current_1, ldown, ldown)
leg2(current_2, ldown, ldown)
leg3(current_3, ldown, ldown)
leg4(current_4, ldown, ldown)

for i in range(32):
    if current_1 == hipin:
        leg_1 = lup
        leg1(current_1, leg_1, leg_1)
        sleep(0.1)
        current_1 = hipout
        leg1(current_1, leg_1, leg_1)
        sleep(0.1)
        leg_1 = ldown
        leg1(current_1, leg_1, leg_1)
        sleep(0.1)
    else:
        current_1 += (hipdiff/3)
    if current_2 == hipout:
        leg_2 = lup
        leg2(current_2, leg_2, leg_2)
        sleep(0.1)
        current_2 = hipin
        leg2(current_2, leg_2, leg_2)
        sleep(0.1)
        leg_2 = ldown
        leg2(current_2, leg_2, leg_2)
        sleep(0.1)
    else:
        current_2 -= (hipdiff/3)
    if current_3 == hipout:
        leg_3 = lup
        leg3(current_3, leg_3, leg_3)
        sleep(0.1)
        current_3 = hipin
        leg3(current_3, leg_3, leg_3)
        sleep(0.1)
        leg_3 = ldown
        leg3(current_3, leg_3, leg_3)
        sleep(0.1)
    else:
        current_3 -= (hipdiff/3)
        leg_3 = ldown
    if current_4 == hipin:
        leg_4 = lup
        leg4(current_4, leg_4, leg_4)
        sleep(0.1)
        current_4 = hipout
        leg4(current_4, leg_4, leg_4)
        sleep(0.1)
        leg_4 = ldown
        leg4(current_4, leg_4, leg_4)
        sleep(0.1)
    else:
        current_4 += (hipdiff/3)
        leg_4 = ldown
    leg1(current_1, leg_1, leg_1)
    leg2(current_2, leg_2, leg_2)
    leg3(current_3, leg_3, leg_3)
    leg4(current_4, leg_4, leg_4)
    sleep(0.2)


















