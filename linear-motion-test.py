from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep

position_1 = [180, 100, 120]

kit.servo[0].angle = 180 - position_1[0]
kit.servo[1].angle = 180 - position_1[1]
kit.servo[2].angle = 180 - position_1[2]


