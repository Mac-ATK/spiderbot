from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep
from approxeng.input.selectbinder import ControllerResource

class RobotStopException(Exception):
    """
    The simplest possible subclass of Exception, we'll raise this if we want to stop the robot
    for any reason. Creating a custom exception like this makes the code more readable later.
    """
    pass

#Matty's controller = 34:AF:2C:19:FE:4B

shoulder = 167.50
elbow = 138
wrist = 131

kit.servo[0].angle = 180 - shoulder
kit.servo[1].angle = 180 - elbow
kit.servo[2].angle = 180 - wrist

min_shoulder = 1
min_elbow = 1
min_wrist = 1

max_shoulder = 179
max_elbow = 179
max_wrist = 179




# Outer try / except catches the RobotStopException we just defined, which we'll raise when we want to
# bail out of the loop cleanly, shutting the motors down. We can raise this in response to a button press
try:
    while True:
        # Inner try / except is used to wait for a controller to become available, at which point we
        # bind to it and enter a loop where we read axis values and send commands to the motors.
        try:
            # Bind to any available joystick, this will use whatever's connected as long as the library
            # supports it.
            with ControllerResource(dead_zone=0.1, hot_zone=0.2) as joystick:
                print('Controller found, press HOME button to exit, use left stick to drive.')
                print(joystick.controls)
                # Loop until the joystick disconnects, or we deliberately stop by raising a
                # RobotStopException
                while joystick.connected:
                    lx_axis, ly_axis, rx_axis, ry_axis = joystick['lx', 'ly', 'rx', 'ry']
                    if rx_axis > 0:
                        if shoulder < max_shoulder:
                            shoulder = shoulder + (rx_axis / 4)
                        else:
                            pass
                    else:
                        if shoulder > min_shoulder:
                            shoulder = shoulder + (rx_axis / 4)
                        else:
                            pass

                    if lx_axis > 0:
                        if elbow < max_elbow:
                            elbow = elbow + (lx_axis / 4)
                        else:
                            pass
                    else:
                        if elbow > min_elbow:
                            elbow = elbow + (lx_axis / 4)
                        else:
                            pass

                    if ly_axis > 0:
                        if wrist < max_wrist:
                            wrist = wrist + (-ly_axis / 4)
                        else:
                            pass
                    else:
                        if wrist > min_wrist:
                            wrist = wrist + (-ly_axis / 4)
                        else:
                            pass
                    
                    kit.servo[0].angle = 180 - shoulder
                    kit.servo[1].angle = 180 - elbow
                    kit.servo[2].angle = 180 - wrist
                    print(shoulder, elbow, wrist)
                    joystick.check_presses()
                    if joystick.has_presses:
                        print(joystick.presses)
                    if 'home' in joystick.presses:
                        raise RobotStopException()
        except IOError:
            # We get an IOError when using the ControllerResource if we don't have a controller yet,
            # so in this case we just wait a second and try again after printing a message.
            print('No controller found yet')
            sleep(1)
except RobotStopException:
    # This exception will be raised when the home button is pressed, at which point we should
    # stop the motors.
    pass