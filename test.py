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

tank = Navigation.tank_init()

# Navigation.distance_goer(tank, 50, 35, 0)


def test():
    init.debug_print(tank.gyro.angle)
    tank.turn_degrees(5, 90-tank.gyro.angle, True, 0.25)
    init.debug_print(tank.gyro.angle)

    tank.turn_degrees(15, -80)
    init.debug_print(tank.gyro.angle)
    tank.turn_degrees(5, -80-tank.gyro.angle, True, 0.25)
    init.debug_print(tank.gyro.angle)

    tank.turn_degrees(15, 63)
    init.debug_print(tank.gyro.angle)
    tank.turn_degrees(5, 63-tank.gyro.angle, True, 0.25)
    init.debug_print(tank.gyro.angle)

    tank.turn_degrees(15, -22)
    init.debug_print(tank.gyro.angle)
    tank.turn_degrees(5, -22-tank.gyro.angle, True, 0.25)
    init.debug_print(tank.gyro.angle)

if __name__ == "__main__":
    test()
