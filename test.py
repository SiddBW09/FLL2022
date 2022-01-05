#!/usr/bin/env python3

'''
Imports:
'''
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B,MoveTank, SpeedPercent, follow_for_ms, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import Navigation
from time import sleep
import time
from ev3dev2.motor import OUTPUT_B, MediumMotor
import Navigation
import init
import claw

tank = MoveTank(OUTPUT_A, OUTPUT_B)
claw = claw.Claw()
lift = MediumMotor(OUTPUT_D)

lift.on_for_rotations(10, 1.5)

if claw.claw_close_5() == 'blocked':
    init.debug_print("Doin Something About it")
elif claw.claw_close_5():

    lift.on_for_rotations(10, -2)
else:
    tank.on_for_rotations(10, 5, -2)
