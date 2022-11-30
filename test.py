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

# tank = Navigation.tank_init()

# Navigation.distance_goer(tank, 50, 35, 0)


def test():
    tank = Navigation.tank_init()
    # Navigation.distance_goer(tank, 50, 30, 0)


    for x in range(1):
        Navigation.distance_goer(tank, 50, 30, 0)
        sleep(1)
        init.debug_print(tank.gyro.angle)
        Navigation.distance_goer(tank, 50, -20, 0)
        init.debug_print(tank.gyro.angle)
        sleep(1)





    #tank.on_for_rotations(-30, -30, 1)
    # init.debug_print(tank.gyro.angle)
    # tank.turn_degrees(5, -90, True, .1)
    # init.debug_print(tank.gyro.angle)

    # tank.turn_degrees(5, -90, True, .1)
    # init.debug_print(tank.gyro.angle)
    # tank.turn_degrees(5, -90, True, .1)
    # init.debug_print(tank.gyro.angle)
    # tank.turn_degrees(5, -90, True, .1)
    # init.debug_print(tank.gyro.angle)
    # tank.turn_degrees(5, 90, True, .1)
    # init.debug_print(tank.gyro.angle)
    # tank.turn_degrees(5, 90, True, .1)
    # init.debug_print(tank.gyro.angle)
    # tank.turn_degrees(5, 90, True, .1)
    # init.debug_print(tank.gyro.angle)
    # tank.turn_degrees(5, 90, True, .1)
    # init.debug_print(tank.gyro.angle)

if __name__ == "__main__":
    test()
