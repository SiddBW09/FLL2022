#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep, time
import Navigation
import init

def Run():
    tank = Navigation.tank_init()
    flipper=LargeMotor(OUTPUT_C)

    time1 = time()
    WateryThingy(tank, flipper)
    FlameThingy(tank, flipper)
    Boxythingy(tank, flipper)
    MoveyThingy(tank, flipper)
    HighFiveyThingy(tank, flipper)
    CaryThingy(tank, flipper)
    time2 = time()
    init.debug_print(time2-time1)

def WateryThingy(tank, flipper):
    tank.gyro.reset()
    flipper.on_for_rotations(30, 0.3)
    Navigation.distance_goer(tank, 33, -25, 0)
    Navigation.gyro_check(tank, 5, 5)
    flipper.on_for_rotations(-30, 0.3)
    Navigation.goer_no_gyro(tank, 6, 20)
    sleep(0.1)
    Navigation.gyro_check(tank, 4, -4)
    sleep(0.1)
    Navigation.gyro_check(tank, 4, -44)
    flipper.on_for_rotations(30, 0.45)

def FlameThingy(tank, flipper):
    tank.gyro.reset()

    Navigation.distance_goer(tank, 11, -20, 0)
    sleep(0.1)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.gyro_check(tank, 5, 0)

    for x in range(3):
        flipper.on_for_rotations(-10, 0.125)
        flipper.on_for_rotations(10, 0.125)

    Navigation.goer_no_gyro(tank, 4.5, 15)
    Navigation.gyro_check(tank, 5,22)
    Navigation.goer_no_gyro(tank, 14, -15)
    Navigation.gyro_check(tank, 3, 0)
    Navigation.gyro_check(tank, 3, 0)


def Boxythingy(tank, flipper):
    tank.gyro.reset()
    flipper.on_for_rotations(-5, 0.085)
    Navigation.goer_no_gyro(tank, 15.2, -15)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.gyro_check(tank, 5, 0)
    flipper.on_for_rotations(30, 0.089)
    Navigation.goer_no_gyro(tank, 7, 10)
    flipper.on_for_rotations(-80, 0.4)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.gyro_check(tank, 5, 0)



def MoveyThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.gyro_check(tank, 5, 35)
    Navigation.gyro_check(tank, 5, 35)
    flipper.on_for_rotations(5, 0.4)
    Navigation.distance_goer(tank, 19, -20, 35)
    flipper.on_for_rotations(-5, 0.14)
    Navigation.gyro_check(tank, 5, 70)
    flipper.on_for_rotations(5, 0.14)
    Navigation.distance_goer(tank, 19, -25, 70)
    flipper.on_for_rotations(-5, 0.14)
    Navigation.gyro_check(tank, 5, 90)

def HighFiveyThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.gyro_check(tank, 5, 25)
    Navigation.distance_goer(tank, 44, -25, 25)
    Navigation.gyro_check(tank, 5, -90)
    flipper.on_for_rotations(5, 0.2)
    Navigation.goer_no_gyro(tank, 12, 25)
    flipper.on_for_rotations(-10, 0.2)
    Navigation.gyro_check(tank, 5, -90)
    Navigation.gyro_check(tank, 5, -90)
    flipper.on_for_rotations(-30, 0.01)


def CaryThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.gyro_check(tank, 10, 45)
    flipper.on_for_rotations(70, 0.2)
    Navigation.goer_no_gyro(tank,15, -5)
    Navigation.gyro_check(tank,10, 0)
    Navigation.gyro_check(tank,10, 0)
    Navigation.goer_no_gyro(tank, 5, -5)
    flipper.on_for_rotations(-70,0.3)

if __name__ == "__main__":
    Run()
