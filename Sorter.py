#!/usr/bin/env python3

from ev3dev.ev3 import *
import os
from time import sleep
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.motor import MediumMotor
from ev3dev2.sensor.logo import ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4


my_tank = MoveTank(OUTPUT_A, OUTPUT_B)
lift = MediumMotor(OUTPUT_D)
claw = MediumMotor(OUTPUT_C)
 # Init Color Sensors

colorRight = ColorSensor(INPUT_2)

colorLeft = ColorSensor(INPUT_3)
# init Gyro Sensor

tank.gyro = GyroSensor(INPUT_1)

tank.gyro.mode='GYRO-ANG'

tank.gyro.reset()
#Moving the Robot
claw.on_for_rotations(49, 3)
lift.on_for_rotations(49, 3)
claw.on_for_rotations(49, -3.5)
lift.on_for_rotations(49, -3)
sleep(0.2)
my_tank.on_for_rotations(20, 20, -.5)
my_tank.on_for_rotations(20, 0, 0.85)
my_tank.on_for_rotations(20, 20, 0.6)
sleep(1)
claw.on_for_rotations(49, 3)
my_tank.on_for_rotations(20, 20, -0.4)
my_tank.on_for_rotations(-15, 15, 0.41)
my_tank.on_for_rotations(20, 20, 2)
