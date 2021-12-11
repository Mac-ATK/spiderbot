from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep
import threading


#trying to get them all to happen at the same time, combination of the leg1(x,y) etc etc
def alllegs(hip1, leg1, hip2, leg2, hip3, leg3, hip4, leg4):
    for i in range(50):
        global current_1, leg_1, current_2,leg_2, current_3, leg_3, current_4, leg_4
        temp_hip1 = round((current_1 * 0.9) + (hip1 * 0.1),0)
        temp_leg1 = round((leg_1 * 0.9) + (leg1 * 0.1),0)
        kit.servo[0].angle = 180 - temp_hip1
        kit.servo[1].angle = 180 - temp_leg1
        kit.servo[2].angle = 180 - temp_leg1
        current_1 = temp_hip1
        leg_1 = temp_leg1
        temp_hip2 = round((current_2 * 0.9) + (hip2 * 0.1),0)
        temp_leg2 = round((leg_2 * 0.9) + (leg2 * 0.1),0)
        kit.servo[3].angle = temp_hip2
        kit.servo[4].angle = temp_leg2
        kit.servo[5].angle = temp_leg2
        current_2 = temp_hip2
        leg_2 = temp_leg2
        temp_hip3 = round((current_3 * 0.9) + (hip3 * 0.1),0)
        temp_leg3 = round((leg_3 * 0.9) + (leg3 * 0.1),0)
        kit.servo[6].angle = 180 - temp_hip3
        kit.servo[7].angle = 180 - temp_leg3
        kit.servo[8].angle = 180 - temp_leg3
        current_3 = temp_hip3
        leg_3 = temp_leg3
        temp_hip4 = round((current_4 * 0.9) + (hip4 * 0.1),0)
        temp_leg4 = round((leg_4 * 0.9) + (leg4 * 0.1),0)
        kit.servo[9].angle = temp_hip4
        kit.servo[10].angle = temp_leg4
        kit.servo[11].angle = temp_leg4
        current_4 = temp_hip4
        leg_4 = temp_leg4
        #sleep(0.05)

    kit.servo[0].angle = 180 - hip1
    kit.servo[1].angle = 180 - leg1
    kit.servo[2].angle = 180 - leg1
    current_1 = hip1
    leg_1 = leg1

    kit.servo[3].angle = hip2
    kit.servo[4].angle = leg2
    kit.servo[5].angle = leg2
    current_2 = hip2
    leg_2 = leg2

    kit.servo[6].angle = 180 - hip3
    kit.servo[7].angle = 180 - leg3
    kit.servo[8].angle = 180 - leg3
    current_3 = hip3
    leg_3 = leg3

    kit.servo[9].angle = hip4
    kit.servo[10].angle = leg4
    kit.servo[11].angle = leg4
    current_4 = hip4
    leg_4 = leg4


def leg1(hip, leg):
    #50 is used because it's about how many cycles for 90% 10% ratio to get to target, change total alongside ratio
    for i in range(50):
        #i had to leard about global variables just for this
        global current_1
        global leg_1
        #figure out the temporary position for the servos based on current position
        temp_hip = round((current_1 * 0.9) + (hip * 0.1),0)
        temp_leg = round((leg_1 * 0.9) + (leg * 0.1),0)
        #move to the temporary position
        kit.servo[0].angle = 180 - temp_hip
        kit.servo[1].angle = 180 - temp_leg
        kit.servo[2].angle = 180 - temp_leg
        #store the new position
        current_1 = temp_hip
        leg_1 = temp_leg
        #sleep(0.05)
    #to round it off and move to the target distance
    kit.servo[0].angle = 180 - hip
    kit.servo[1].angle = 180 - leg
    kit.servo[2].angle = 180 - leg
    #store that position
    current_1 = hip
    leg_1 = leg

def leg2(hip, leg):
    for i in range(50):
        global current_2
        global leg_2
        temp_hip = round((current_2 * 0.9) + (hip * 0.1),0)
        temp_leg = round((leg_2 * 0.9) + (leg * 0.1),0)
        kit.servo[3].angle = temp_hip
        kit.servo[4].angle = temp_leg
        kit.servo[5].angle = temp_leg
        current_2 = temp_hip
        leg_2 = temp_leg
        #sleep(0.05)
    kit.servo[3].angle = hip
    kit.servo[4].angle = leg
    kit.servo[5].angle = leg
    current_2 = hip
    leg_2 = leg

def leg3(hip, leg):
    for i in range(50):
        global current_3
        global leg_3
        temp_hip = round((current_3 * 0.9) + (hip * 0.1),0)
        temp_leg = round((leg_3 * 0.9) + (leg * 0.1),0)
        kit.servo[6].angle = 180 - temp_hip
        kit.servo[7].angle = 180 - temp_leg
        kit.servo[8].angle = 180 - temp_leg
        current_3 = temp_hip
        leg_3 = temp_leg
        #sleep(0.05)
    kit.servo[6].angle = 180 - hip
    kit.servo[7].angle = 180 - leg
    kit.servo[8].angle = 180 - leg
    current_3 = hip
    leg_3 = leg

def leg4(hip, leg):
    for i in range(50):
        global current_4
        global leg_4
        temp_hip = round((current_4 * 0.9) + (hip * 0.1),0)
        temp_leg = round((leg_4 * 0.9) + (leg * 0.1),0)
        kit.servo[9].angle = temp_hip
        kit.servo[10].angle = temp_leg
        kit.servo[11].angle = temp_leg
        current_4 = temp_hip
        leg_4 = temp_leg
        #sleep(0.05)
    kit.servo[9].angle = hip
    kit.servo[10].angle = leg
    kit.servo[11].angle = leg
    current_4 = hip
    leg_4 = leg


hipin = 180
hipout = 90

ldown = 140
lup = 180

hipdiff = hipin - hipout

current_1 = hipin
current_2 = hipin
current_3 = hipin-((hipdiff/3)*2)
current_4 = hipin-((hipdiff/3)*2)

targ_current_1 = hipin
targ_current_2 = hipin
targ_current_3 = hipin-((hipdiff/3)*2)
targ_current_4 = hipin-((hipdiff/3)*2)

leg_1 = ldown
leg_2 = ldown
leg_3 = ldown
leg_4 = ldown

targ_leg_1 = ldown
targ_leg_2 = ldown
targ_leg_3 = ldown
targ_leg_4 = ldown

kit.servo[0].angle = 180 - current_1
kit.servo[1].angle = 180 - leg_1
kit.servo[2].angle = 180 - leg_1
kit.servo[3].angle = current_2
kit.servo[4].angle = leg_2
kit.servo[5].angle = leg_2
kit.servo[6].angle = 180 - current_3
kit.servo[7].angle = 180 - leg_3
kit.servo[8].angle = 180 - leg_3
kit.servo[9].angle = current_4
kit.servo[10].angle = leg_4
kit.servo[11].angle = leg_4

#leg1(current_1, ldown)
#leg2(current_2, ldown)
#leg3(current_3, ldown)
#leg4(current_4, ldown)

for i in range(32):
    if current_1 == hipin:
        targ_leg_1 = lup
        leg1(targ_current_1, targ_leg_1)
        targ_current_1 = hipout
        leg1(targ_current_1, targ_leg_1)
        targ_leg_1 = ldown
        leg1(targ_current_1, targ_leg_1)
    else:
        targ_current_1 += (hipdiff/3)
    if current_2 == hipout:
        targ_leg_2 = lup
        leg2(targ_current_2, targ_leg_2)
        targ_current_2 = hipin
        leg2(targ_current_2, targ_leg_2)
        targ_leg_2 = ldown
        leg2(targ_current_2, targ_leg_2)
    else:
        targ_current_2 -= (hipdiff/3)
    if current_3 == hipout:
        targ_leg_3 = lup
        leg3(targ_current_3, targ_leg_3)
        targ_current_3 = hipin
        leg3(targ_current_3, targ_leg_3)
        targ_leg_3 = ldown
        leg3(targ_current_3, targ_leg_3)
    else:
        targ_current_3 -= (hipdiff/3)
        targ_leg_3 = ldown
    if current_4 == hipin:
        targ_leg_4 = lup
        leg4(targ_current_4, targ_leg_4)
        targ_current_4 = hipout
        leg4(targ_current_4, targ_leg_4)
        targ_leg_4 = ldown
        leg4(targ_current_4, targ_leg_4)
    else:
        targ_current_4 += (hipdiff/3)
        targ_leg_4 = ldown
    #leg1(current_1, leg_1)
    #leg2(current_2, leg_2)
    #leg3(current_3, leg_3)
    #leg4(current_4, leg_4)
    #sleep(0.2)
    alllegs(targ_current_1, targ_leg_1, targ_current_2, targ_leg_2, targ_current_3, targ_leg_3, targ_current_4, targ_leg_4)


















