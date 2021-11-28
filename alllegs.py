from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep
import threading

def alllegs(hip1, leg1, hip2, leg2, hip3, leg3, hip4, leg4):
    for i in range(50):
        global current_1
        global leg_1
        global current_2
        global leg_2
        global current_3
        global leg_3
        global current_4
        global leg_4
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
        sleep(0.05)

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





#hip works good 90 to 180
#legs work good 100 to 180

#define starting positions
current_1 = 110
current_2 = 110
current_3 = 110
current_4 = 110
leg_1 = 100
leg_2 = 100
leg_3 = 100
leg_4 = 100
#set the starting positions
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


#"animation" here

alllegs(current_1, leg_1, current_2, leg_2, current_3, leg_3, current_4, leg_4)

alllegs(current_1, 0, current_2, leg_2, current_3, leg_3, current_4, leg_4)

alllegs(current_1, 180, current_2, leg_2, current_3, leg_3, current_4, leg_4)

alllegs(current_1, leg_1, current_2, leg_2, current_3, leg_3, current_4, leg_4)


















