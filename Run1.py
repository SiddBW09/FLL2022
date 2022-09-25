#!/usr/bin/env python3

import ev3dev.ev3
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, MoveTank, SpeedPercent, follow_for_ms, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import Navigation
import time
from time import sleep
from ev3dev2.motor import OUTPUT_B, MediumMotor
import init

def run1():
    tank = Navigation.tank_init()

    # ex: tank.on_for_rotations(30, 30, 1) #forward (left speed(rpm), right speed(rpm), rotations)
    # ex: tank.turn_degrees(20, 45, True, .1) #turn(speed, degrees, brake after turning, accuracy)

    # ex: Navigation.distance_goer(tank, 30, 30, 7) #move better(tank, distancecm, speed, angle currently at)
    # ex: Navigation.gyro_check(tank, 1, 7) #ACCURATE TURNING(tank, speed, degrees)
    Navigation.distance_goer(tank,5,-30,0)
    # Navigation.gyro_check(tank,30,-45)
    # Navigation.distance_goer(tank,4s0,-30,-45)

if __name__ == "__main__":
    run1()
