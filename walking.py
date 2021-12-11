from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep

positions = [
    [161.44, 171.10, 133.51],
    [108.91, 159.28, 107.39],
    [81, 106.29, 4.56]
]

legs = {
    "leg1" : [kit.servo[0].angle, kit.servo[1].angle, kit.servo[2].angle], 
    "leg2" : [kit.servo[3].angle, kit.servo[4].angle, kit.servo[5].angle],
    "leg3" : [kit.servo[6].angle, kit.servo[7].angle, kit.servo[8].angle],
    "leg4" : [kit.servo[9].angle, kit.servo[10].angle, kit.servo[11].angle]
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
        legs[leg][i] = leg_positions[leg][i]
        print(legs[leg][i])

