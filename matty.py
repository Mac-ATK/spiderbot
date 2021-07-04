from adafruit_servokit import ServoKit
kit = ServoKit(channels=2)

kit.servo[0].angle = 90
kit.servo[1].angle = 90