#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep, time
import Navigation
import init

def PlatformRun(tank, flipper):
    flip_flop = MediumMotor(OUTPUT_D)
    tank.gyro.reset()
    flipper.reset()
    AnotherWateryThingy(tank, flipper)

    #WateryThingy(tank, flipper)
    FlameThingy(tank, flipper)

    Boxythingy(tank, flipper)
    return

    NewyCody(tank, flipper)
    HighFiveyThingy(tank, flipper)
    #MoveyThingy(tank, flipper)

    # # CaryThingy(tank, flipper)

def AnotherWateryThingy(tank, flipper):
    flipper.on_for_rotations(30, 0.3)
    Navigation.distance_goer(tank, 44, -30, 0)
    Navigation.gyro_check(tank, 5, 50)
    #init.debug_print("before flip", tank.gyro.angle)
    flipper.on_for_rotations(-30, 0.2)
    #Navigation.goer_no_gyro(tank, 10, 10)
    Navigation.gyro_check(tank, 5, 0)
    flipper.on_for_rotations(30, 0.35)

'''def WateryThingyOld(tank, flipper):
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
    flipper.on_for_rotations(30, 0.45)'''

def WateryThingy(tank, flipper):
    tank.gyro.reset()
    flipper.on_for_rotations(30, 0.3)
    Navigation.distance_goer(tank, 35, -25, 0)
    Navigation.gyro_check(tank, 5, 5)
    flipper.on_for_rotations(-30, 0.3)
    Navigation.goer_no_gyro(tank, 8, 20)
    sleep(0.1)
    Navigation.gyro_check(tank, 4, -4)
    sleep(0.1)
    Navigation.gyro_check(tank, 4, -45)
    flipper.on_for_rotations(30, 0.1)

def FlameThingy(tank, flipper):
    #tank.gyro.reset()

    Navigation.distance_goer(tank, 9.5, -20, 0)
    #init.debug_print("before plat ",tank.gyro.angle)
    #Navigation.gyro_check(tank, 5, 0)

    for x in range(2):
        flipper.on_for_rotations(-15, 0.12)
        flipper.on_for_rotations(15, 0.12)
    flipper.on_for_rotations(-20, 0.12)

    Navigation.distance_goer(tank, 4.5, 15, 0)
    #init.debug_print("first move: ",tank.gyro.angle)
    Navigation.gyro_check(tank, 10, 22)
    #init.debug_print("After first gyro check: ",tank.gyro.angle)
    Navigation.distance_goer(tank, 14, -15,22)
    #init.debug_print("second move: ",tank.gyro.angle)
    Navigation.gyro_check(tank, 5, 0)
    #init.debug_print("After second gyro check: ",tank.gyro.angle)



def Boxythingy(tank, flipper):
    #flipper.on_for_rotations(-5, 0.085)
    Navigation.goer_no_gyro(tank, 12, -15)
    #Navigation.gyro_check(tank, 5, 5)
    flipper.on_for_rotations(30, 0.12)
    Navigation.goer_no_gyro(tank, 7, 10)
    flipper.on_for_rotations(-80, 0.45)
    Navigation.gyro_check(tank, 10, 45)
    Navigation.goer_no_gyro(tank, 8, -10)
    Navigation.gyro_check(tank, 10, 90)


def MoveyThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.gyro_check(tank, 10, 35)
    flipper.on_for_rotations(10, 0.4)
    Navigation.distance_goer(tank, 19, -25, 35)
    flipper.on_for_rotations(-10, 0.14)
    Navigation.gyro_check(tank, 5, 70)
    flipper.on_for_rotations(10, 0.14)
    Navigation.distance_goer(tank, 19, -30, 70)
    Navigation.gyro_check(tank, 5, 90)

def NewyCody(tank, flipper):
    flip_flop = MediumMotor(OUTPUT_D)

    #Go and sweep nrg units
    Navigation.goer_no_gyro(tank, -17, 20)
    Navigation.gyro_check(tank, 5, 90)




    flip_flop.on_for_rotations(20, -0.35)
    Navigation.distance_goer(tank, 23, -50, 90)
    Navigation.gyro_check(tank, 5, 135)
    flip_flop.on_for_rotations(20, 0.35)
    Navigation.distance_goer(tank, 32.5, -20, 135)
    init.debug_print(tank.gyro.angle)
    Navigation.gyro_check(tank, 10, 3)
    init.debug_print(tank.gyro.angle)

def HighFiveyThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.goer_no_gyro(tank, -15, 10)
    flipper.on_for_rotations(10, 0.5)
    Navigation.goer_no_gyro(tank, 4.5, 10)
    Navigation.gyro_check(tank, 5, 0)
    flipper.on_for_rotations(-30, 0.4)
    Navigation.gyro_check(tank, 5, 0)

def CaryThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.distance_goer(tank, 3, -15, 0)
    Navigation.gyro_check(tank, 10, 90)
    Navigation.distance_goer(tank, 35, -25, 90)
    init.debug_print(tank.gyro.angle)
    Navigation.gyro_check(tank, 5, -50)
    flipper.on_for_rotations(15, 0.65)

    # Navigation.gyro_check(tank, 5, -43)
    # Navigation.goer_no_gyro(tank, 6, -10)
    # Navigation.gyro_check(tank, 5, -36)
    # flipper.on_for_rotations(15, -0.4)
    # Navigation.gyro_check(tank, 5, -50)
    # Navigation.goer_no_gyro(tank, 84, 50)

def DinoRun(tank, flipper):
    flipper.on_for_rotations(-10, 0.05)
    tank.gyro.reset()
    Navigation.distance_goer(tank, 163, -60, 0)

if __name__ == "__main__":
    tank = Navigation.tank_init()
    flipper = LargeMotor(OUTPUT_C)
    time1 = time()
    PlatformRun(tank, flipper)
    init.debug_print(time()-time1)
