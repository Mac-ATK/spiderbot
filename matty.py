from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep

hipmax = 50
#hipmin = 180
hipmin = 130


#ldown = 0
ldown = 0
#lup = 180
lup = 140

def leg1(angle1, angle2, angle3):
    kit.servo[0].angle = 180 - angle1
    kit.servo[1].angle = 180 - angle2
    kit.servo[2].angle = 180 - angle3

def leg2(angle1, angle2, angle3):
    kit.servo[3].angle = angle1
    kit.servo[4].angle = angle2
    kit.servo[5].angle = angle3

def leg3(angle1, angle2, angle3):
    kit.servo[6].angle = 180 - angle1
    kit.servo[7].angle = 180 - angle2
    kit.servo[8].angle = 180 - angle3

def leg4(angle1, angle2, angle3):
    kit.servo[9].angle = angle1
    kit.servo[10].angle = angle2
    kit.servo[11].angle = angle3

angle_leg = lup
angle_hip = hipmin

leg1(hipmin, 180, 0)
leg2(hipmin, 90, 90)
leg3(90, 90, 90)
leg4(140, 90, 90)

sleep(0.2)
leg1(0, 180, 0)

sleep(0.2)
leg1(180, 180, 0)

sleep(0.2)
leg1(0, 180, 0)

sleep(0.2)
leg1(180, 180, 0)







    
    