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
base_motor = Motor.(Port.A)
elbow_motor = Motor.(Port.B)
end_motor = Motor.(Port.C)

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
    end_motor.run_angle(10, 45) # lift the pen by 45 degrees, + or - can be later adjusted
    end_motor.hold()
    wait(1000)

### Dorpping down the pen
def lift_wrist():
    end_motot.run_angle(10, -45) # drop down the pen by 45 degrees back, + or - can be later adjusted
    end_motot.hold()
    wait(1000)


## Use the matlab file from Mechanism to wirte the logic
### Draw a vertical line
def draw_vertical_line(length):
    

### Draw a perpendicular line
def draw_perpendicular_line(length):