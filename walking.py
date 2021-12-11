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
    "leg1" : positions[0],
    "leg2" : positions[0],
    "leg3" : positions[1],
    "leg4" : positions[1]
}

for leg in legs:
    print(leg)
    for i in range(len(legs[leg])):
        legs[leg][i].angle = leg_positions[leg][i]
        print(legs[leg][i])

