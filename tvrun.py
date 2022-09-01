#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep
import Navigation, init

tank = Navigation.tank_init()

Navigation.distance_goer(tank, 40, 30, 0)
sleep(1)
Navigation.distance_goer(tank, 5, -30, 0)
sleep(1)
Navigation.gyro_check(tank, 5, -45)
Navigation.distance_goer(tank, 40, 30, -45)
Navigation.gyro_check(tank, 5, 50)
Navigation.distance_goer(tank, 10, 30, 50)
for x in range(3):
    Navigation.distance_goer(tank, 30, 30, 50)
    sleep(1)
    Navigation.distance_goer(tank, 15, -30, 50)
    Navigation.gyro_check(tank, 5, 50)
