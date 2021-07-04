from adafruit_servokit import ServoKit
kit = ServoKit(channels=8)
from time import sleep

kit.servo[0].angle = 0
kit.servo[1].angle = 0

sleep(2)

kit.servo[0].angle = 180

sleep(2)

kit.servo[1].angle = 180

sleep(1)

kit.servo[0].angle = 0
kit.servo[1].angle = 0

sleep(1)

kit.servo[0].angle = 180
kit.servo[1].angle = 180
