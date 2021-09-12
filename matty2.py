from adafruit_servokit import ServoKit
kit = ServoKit(channels=8)
from time import sleep

def leg1(angle1, angle2):
    kit.servo[0].angle = 180 - angle1
    kit.servo[1].angle = 180 - angle2


leg1(0, 0)
sleep(1)
leg1(180, 180)
sleep(1)
leg1(180, 0)
sleep(0.2)
leg1(180, 180)
sleep(0.2)
leg1(180, 0)
sleep(0.2)
leg1(180, 180)

sleep(1)

leg1(0, 180)
sleep(0.2)
leg1(180, 180)
sleep(0.2)
leg1(0, 180)
sleep(0.2)
leg1(180, 180)
sleep(0.2)

sleep(1)

leg1(0, 0)
sleep(0.3)
leg1(180, 180)
sleep(0.3)
leg1(0, 0)
sleep(0.3)
leg1(180, 180)









