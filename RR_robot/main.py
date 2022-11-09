#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

## Adjust the port order here
base_motor = Motor(Port.A)
elbow_motor = Motor(Port.B)
end_motor = Motor(Port.C)

# The robot layout should be like this in the initial state
#                                          
#         ____ A_____B_____C                                    
#        |base|                                            
#        |    |                                         
#


# Write your program here.


# Hold RR robot related functions

## Pen lifting
### Lifting the pen
def lift_wrist():
    end_motor.run_angle(40, 45) # lift the pen by 45 degrees, + or - can be later adjusted
    end_motor.hold()
    wait(1000)

### Dropping down the pen
def drop_wrist():
    end_motor.run_angle(40, -45) # drop down the pen by 45 degrees back, + or - can be later adjusted
    end_motor.hold()
    wait(1000)

