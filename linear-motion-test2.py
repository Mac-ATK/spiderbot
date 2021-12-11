from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep



## t_ means target p_ meansposition
def leg1(shoulder, elbow, wrist):
    #50 is used because it's about how many cycles for 90% 10% ratio to get to target, change total alongside ratio
    for i in range(50):
        #i had to leard about global variables just for this
        global p_shoulder
        global p_elbow
        global p_wrist
        #figure out the temporary position for the servos based on current position
        t_shoulder = round((p_shoulder * 0.9) + (shoulder * 0.1),0)
        t_elbow = round((p_elbow * 0.9) + (elbow * 0.1),0)
        t_wrist = round((p_wrist * 0.9) + (wrist * 0.1),0)
        #move to the temporary position
        kit.servo[0].angle = 180 - t_shoulder
        kit.servo[1].angle = 180 - t_elbow
        kit.servo[2].angle = 180 - t_wrist
        #store the new position
        p_shoulder = t_shoulder
        p_elbow = t_elbow
        p_wrist = t_wrist
        sleep(0.05)
    #to round it off and move to the target distance
    kit.servo[0].angle = 180 - shoulder
    kit.servo[1].angle = 180 - elbow
    kit.servo[2].angle = 180 - wrist
    #store that position
    p_shoulder = shoulder
    p_elbow = elbow
    p_wrist = wrist




target = [180, 140, 100]

def set_legs():
    global position
    kit.servo[0].angle = 180 - position[0]
    kit.servo[1].angle = 180 - position[1]
    kit.servo[2].angle = 180 - position[2]
    #kit.servo[3].angle = position[3]
    #kit.servo[4].angle = position[4]
    #kit.servo[5].angle = position[5]
    #kit.servo[6].angle = 180 - position[6]
    #kit.servo[7].angle = 180 - position[7]
    #kit.servo[8].angle = 180 - position[8]
    #kit.servo[9].angle = position[9]
    #kit.servo[10].angle = position[10]
    #kit.servo[11].angle = position[11]

def alllegs(shoulder1, elbow1, wrist1, shoulder2, elbow2, wrist2, shoulder3, elbow3, wrist3, shoulder4, elbow4, wrist4):
    global position
    for i in range(35):
        temp1 = (position[0] * 0.9) + (shoulder1 * 0.1)
        temp2 = (position[1] * 0.9) + (elbow1 * 0.1)
        temp3 = (position[2] * 0.9) + (wrist1 * 0.1)
        temp4 = (position[3] * 0.9) + (shoulder2 * 0.1)
        temp5 = (position[4] * 0.9) + (elbow2 * 0.1)
        temp6 = (position[5] * 0.9) + (wrist2 * 0.1)
        temp7 = (position[6] * 0.9) + (shoulder3 * 0.1)
        temp8 = (position[7] * 0.9) + (elbow3 * 0.1)
        temp9 = (position[8] * 0.9) + (wrist3 * 0.1)
        temp10 = (position[9] * 0.9) + (shoulder4 * 0.1)
        temp11 = (position[10] * 0.9) + (elbow4 * 0.1)
        temp12 = (position[11] * 0.9) + (wrist4 * 0.1)

        kit.servo[0].angle = 180 - temp1
        kit.servo[1].angle = 180 - temp2
        kit.servo[2].angle = 180 - temp3
        #kit.servo[3].angle = temp4
        #kit.servo[4].angle = temp5
        #kit.servo[5].angle = temp6
        #kit.servo[6].angle = 180 - temp7
        #kit.servo[7].angle = 180 - temp8
        #kit.servo[8].angle = 180 - temp9
        #kit.servo[9].angle = temp10
        #kit.servo[10].angle = temp11
        #kit.servo[11].angle = temp12
        
        position[0] = temp1
        position[1] = temp2
        position[2] = temp3
        position[3] = temp4
        position[4] = temp5
        position[5] = temp6
        position[6] = temp7
        position[7] = temp8
        position[8] = temp9
        position[9] = temp10
        position[10] = temp11
        position[11] = temp12
        
        print(temp1)
        sleep(0.05)

    position[0] = shoulder1
    position[1] = elbow1
    position[2] = wrist1
    position[3] = shoulder2
    position[4] = elbow2
    position[5] = wrist2
    position[6] = shoulder3
    position[7] = elbow3
    position[8] = wrist3
    position[9] = shoulder4
    position[10] = elbow4
    position[11] = wrist4
    kit.servo[0].angle = 180 - temp1
    kit.servo[1].angle = 180 - temp2
    kit.servo[2].angle = 180 - temp3
    #kit.servo[3].angle = temp4
    #kit.servo[4].angle = temp5
    #kit.servo[5].angle = temp6
    #kit.servo[6].angle = 180 - temp7
    #kit.servo[7].angle = 180 - temp8
    #kit.servo[8].angle = 180 - temp9
    #kit.servo[9].angle = temp10
    #kit.servo[10].angle = temp11
    #kit.servo[11].angle = temp12


####
####
####alllegs(*t_position)
####t_position[1] = 150
####t_position[0] = 164
####t_position[2] = 134
####alllegs(*t_position)
####
####t_position[0] = 136
####t_position[1] = 148
####t_position[2] = 124
####alllegs(*t_position)
####
####t_position[0] = 113
####t_position[1] = 140
####t_position[2] = 106
####alllegs(*t_position)
####
####t_position[0] = 96
####t_position[1] = 119
####t_position[2] = 71
####alllegs(*t_position)
####
####t_position[0] = 84
####t_position[1] = 79
####t_position[2] = 1
####alllegs(*t_position)
####
####

position = [161.44, 171.10, 133.51]
p_shoulder = position[0]
p_elbow = position[1]
p_wrist = position[2]


kit.servo[0].angle = 180 - p_shoulder
kit.servo[1].angle = 180 - p_elbow
kit.servo[2].angle = 180 - p_wrist

target = [161.44, 171.10, 133.51]

leg1(*target)

#target = [142.5, 134, 127]

#leg1(*target)

#target = [120.5, 124, 110.5]

#leg1(*target)

target = [110.61, 157.37, 105.84]

leg1(*target)

target = [81, 106.29, 4.56]

leg1(*target)