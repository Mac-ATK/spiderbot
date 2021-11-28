from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep


# starting positions, always update this value
hippos = 120
legpos = 20

#set the bot to the starting positions - hips
kit.servo[0].angle = 180 - hippos
kit.servo[3].angle = hippos
kit.servo[6].angle = 180 - hippos
kit.servo[9].angle = hippos

#legs
kit.servo[1].angle = 180 - legpos
kit.servo[2].angle = 180 - legpos
kit.servo[4].angle = legpos
kit.servo[5].angle = legpos
kit.servo[7].angle = 180 - legpos
kit.servo[8].angle = 180 -  legpos
kit.servo[10].angle = legpos
kit.servo[11].angle = legpos


def hip3(angle1, angle2):
    for i in range(50):
        global hippos
        global legpos
        temptarget = round((hippos * 0.9) + (angle1 * 0.1),0)
        temptarget2 = (legpos * 0.9) + (angle2 * 0.1)
        kit.servo[6].angle = 180 - temptarget
        kit.servo[7].angle = 180 - temptarget2
        kit.servo[8].angle = 180 - temptarget2
        hippos = temptarget
        legpos = temptarget2
        sleep(0.025)
    kit.servo[6].angle = 180 - angle1
    kit.servo[7].angle = 180 - angle2
    kit.servo[8].angle = 180 - angle2
    hippos = angle1
    legpos = angle2


#just updates the legs
def combolegs(angle1):
    for i in range(50):
        global legpos
        temptarget = (legpos * 0.9) + (angle1 * 0.1)
        legpos = temptarget
        sleep(0.05)
        kit.servo[1].angle = 180 - temptarget
        kit.servo[2].angle = 180 - temptarget
        kit.servo[4].angle = temptarget
        kit.servo[5].angle = temptarget
        kit.servo[7].angle = 180 - temptarget
        kit.servo[8].angle = 180 -  temptarget
        kit.servo[10].angle = temptarget
        kit.servo[11].angle = temptarget
    legpos = angle1
    kit.servo[1].angle = 180 - legpos
    kit.servo[2].angle = 180 - legpos
    kit.servo[4].angle = legpos
    kit.servo[5].angle = legpos
    kit.servo[7].angle = 180 - legpos
    kit.servo[8].angle = 180 -  legpos
    kit.servo[10].angle = legpos
    kit.servo[11].angle = legpos





sleep(0.5)
combolegs(160)
combolegs(20)
combolegs(160)
combolegs(20)
combolegs(160)



















