from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep
import threading

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

hipin = 50
hipout = 180
hipstable = 140

ldown = 0
lup = 180

sleeptime = 1
leg1_thread = threading.Thread(target=leg1, args=(hipstable, lup, lup))
leg2_thread = threading.Thread(target=leg2, args=(hipstable, lup, lup))
leg3_thread = threading.Thread(target=leg3, args=(hipstable, lup, lup))
leg4_thread = threading.Thread(target=leg4, args=(hipstable, lup, lup))

leg1_thread.start()
leg2_thread.start()
leg3_thread.start()
leg4_thread.start()


#sleep(5)

#leg1_thread2 = threading.Thread(target=leg1, args=(hipstable, lup, lup), daemon=True)
#leg2_thread2 = threading.Thread(target=leg2, args=(hipstable, lup, lup), daemon=True)
#leg3_thread2 = threading.Thread(target=leg3, args=(hipstable, lup, lup), daemon=True)
#leg4_thread2 = threading.Thread(target=leg4, args=(hipstable, lup, lup), daemon=True)

#leg1_thread2.start()
#leg2_thread2.start()
#leg3_thread2.start()
#leg4_thread2.start()

#leg1(hipstable, ldown, ldown)
#leg2(hipstable, ldown, ldown)
#leg3(hipstable, ldown, ldown)
#leg4(hipstable, ldown, ldown)
















