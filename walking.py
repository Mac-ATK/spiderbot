from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep

positions = [
    [161.44, 171.10, 133.51],
    [108.91, 159.28, 107.39],
    [81, 106.29, 4.56]
]

legs = {
    "leg1" : [kit.servo[0], kit.servo[1], kit.servo[2]], 
    "leg2" : [kit.servo[3], kit.servo[4], kit.servo[5]],
    "leg3" : [kit.servo[6], kit.servo[7], kit.servo[8]],
    "leg4" : [kit.servo[9], kit.servo[10], kit.servo[11]]
}

leg_positions = {
    "leg1" : positions[1],
    "leg2" : positions[0],
    "leg3" : positions[0],
    "leg4" : positions[1]
}

leg_targets = {
    "leg1" : 1,
    "leg2" : 0,
    "leg3" : 0,
    "leg4" : 1
}

for leg in legs:
    for i in range(len(legs[leg])):
        if leg in ["leg1", "leg3"]:
            legs[leg][i].angle = 180 - leg_positions[leg][i]
        else: 
            legs[leg][i].angle = leg_positions[leg][i]

def all_legs():
    global leg_positions
    for i in range(50): # Gradual move
        for leg in legs:
            for i in range(len(legs[leg])):
                temp = round((leg_positions[leg][i] * 0.9) + (positions[leg_targets[leg]][i] * 0.1),0)
                if leg in ["leg1", "leg3"]: 
                    legs[leg][i].angle = 180 - temp
                else: 
                    legs[leg][i].angle = temp
                leg_positions[leg][i] = temp
    
    for leg in legs: # Final set to exact angle
        for i in range(len(legs[leg])):
            if leg in ["leg1", "leg3"]: 
                legs[leg][i].angle = 180 - positions[leg_targets[leg]][i]
            else: 
                legs[leg][i].angle = positions[leg_targets[leg]][i]
            leg_positions[leg][i] = positions[leg_targets[leg]][i]

def reset_leg(leg):
    global leg_positions
    legs[leg][1].angle = 180
    leg_positions[leg][1] = 180
    for i in range(50): # Gradual move
        for i in range(len(legs[leg])):
            temp = round((leg_positions[leg][i] * 0.9) + (leg_targets[leg][i] * 0.1),0)
            if leg in ["leg1", "leg3"]: 
                legs[leg][i].angle = 180 - temp
            else: 
                legs[leg][i].angle = temp
            leg_positions[leg][i] = temp
    
    for i in range(len(legs[leg])):
        if leg in ["leg1", "leg3"]: 
            legs[leg][i].angle = 180 - leg_targets[leg][i]
        else: 
            legs[leg][i].angle = leg_targets[leg][i]
        leg_positions[leg][i] = leg_targets[leg][i]


while True:
    for leg in reversed(legs): 
        if leg in ["leg1", "leg2"]:
            leg_targets[leg] -= 1
            if leg_targets[leg] < 0:
                leg_targets[leg] = 2
                reset_leg(leg)
                leg_targets[leg] = 1
        else:
            leg_targets[leg] += 1
            if leg_targets[leg] > 2:
                leg_targets[leg] = 0
                reset_leg(leg)
                leg_targets[leg] = 1
    all_legs()
