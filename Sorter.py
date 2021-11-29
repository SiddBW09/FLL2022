#!/usr/bin/env python3

import ev3dev.ev3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from time import sleep
from ev3dev2.sound import Sound
import init
import claw
import Navigation



def current_run():

    init.debug_print("In current run")
    my_tank = Navigation.tank_init()
    lift = MediumMotor(OUTPUT_D)
    MyClaw = claw.Claw()
    MyClaw.claw.reset()
    Have_brick(lift)






def SlotToCircle(x):
    #move to
    my_tank.on_for_rotations(15, 15, -0.3)
    my_tank.on_for_rotations(15, 0, 0.85)
    my_tank.on_for_rotations(25, 25, x)
    lift.on_for_rotations(49, 3)
    sleep(0.5)
    claw.claw_open(100)

def CircleToSlot():
    my_tank.on_for_rotations(15, 15, -0.75)
    my_tank.on_for_rotations(-15, 15, 0.5)
    my_tank.on_for_rotations(15, 15, 0.2)


def no_detection():
    claw.claw_open(100)
    lift.on_for_rotations(49, -3)
    my_tank.on_for_rotations(15, 15, 0.3)
    claw.claw_open(100)
    lift.on_for_rotations(49, 3)
    claw.claw_close(100)
    lift.on_for_rotations(49, -3)


def Have_brick(lift):

    init.debug_print("Have brick")
    i = 0
    lift.reset()
    while True:
        init.debug_print("In loop")
        lift.on_for_rotations(5, 0.1, brake=False)
        init.debug_print(lift.state)
        if 'stalled' in lift.state:
            init.debug_print(lift.state)
            break
        i += 1
    init.debug_print(i)
    if (i > 15):
     return False
    return True





#
'''claw.claw_open(100)
lift.on_for_rotations(49, 2.5)
if claw.claw_close(100):
    lift.on_for_rotations(49, -3)
    SlotToCircle(0.85)
    lift.on_for_rotations(49, 3)
    sleep(1)
    claw.claw_open(100)
    sleep(0.5)
    lift.on_for_rotations(49, -3)
    CircleToSlot()
else:
    no_detection()
    my_tank.on_for_rotations(15, 15, -0.3)
    SlotToCircle(0.85)'''


'''my_tank.on_for_rotations(15, 15, 0.15)
claw.claw_open(100)
sleep(0.5)
lift.on_for_rotations(49, 3)
sleep(0.5)
claw.claw_close(100)
sleep(0.5)
lift.on_for_rotations(49, -3)'''


current_run()


