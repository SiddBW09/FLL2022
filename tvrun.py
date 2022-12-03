#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep, time
import Navigation
import threading
import init
def tv():
    colorful_flipper=LargeMotor(OUTPUT_C)
    tank = Navigation.tank_init()

    #Lower flipper
    colorful_flipper.on_for_rotations(10, 0.4)

    #Tv run 1.3
    #OG distance = 14
    Navigation.goer_no_gyro(tank, 12, -30)
    #tank.on_for_rotations(-20, -20, 1)

    #Lift flipper
    colorful_flipper.on_for_rotations(-10, 0.4)

    #Turn left OG val -45
    Navigation.gyro_check(tank, 5, -42)
    init.debug_print("Should be -42:", tank.gyro.angle)

    #tank.turn_degrees(10, -30, True, 0.1)

    #Lift flippy
    #colorful_flipper.on_for_rotations(10, -0.25)

    #Pause
    #sleep(2)

    #Parallel to windmill go
    Navigation.goer_no_gyro(tank, 53, -30)

    #Turn almost all the way
    Navigation.gyro_check(tank, 5, 40)
    init.debug_print("Should be 40:", tank.gyro.angle)

    #Go forward from
    Navigation.goer_no_gyro(tank, 2, -15)

    #NEW code go back
    #Navigation.goer_no_gyro(tank, 2, 20)

    #Lower flipper
    colorful_flipper.on_for_rotations(5, 0.4)


    #Turns all the way OG used to not be commented: 👇
    #4tank.turn_degrees(5, 2, True, 0.1)
    #tank.turn_degrees(20, 1)
    #Put colorful flipper down

    return

    #Go forward a little
    Navigation.goer_no_gyro(tank, 1, -10)

    #Turn colorful flipper into place
    tank.turn_degrees(10, 45, True, 0.1)
    quit()
def windmill():

    colorful_flipper=LargeMotor(OUTPUT_C)
    tank = Navigation.tank_init()

    #Push windmill OG val -15, 0.4 rotations
    time1 = time()
    for x in range(3):
        tank.on_for_rotations(-10, -10, 0.27)
        tank.on_for_rotations(7, 7, 0.24)
def toystory3():

    colorful_flipper = LargeMotor(OUTPUT_C)
    tank = Navigation.tank_init()

   # Navigation.goer_no_gyro(tank, 5.5, 20)

    #Lift colorful flipper Og val 5, -0.25
    Navigation.gyro_check(tank, 5, -20)
    init.debug_print("Should be -20:", tank.gyro.angle)
    colorful_flipper.on_for_rotations(7, -0.35)

    sleep(1)
    Navigation.gyro_check(tank, 5, -165)
    init.debug_print("Should be -165:", tank.gyro.angle)
    Navigation.goer_no_gyro(tank, 3, 20)

    #Rotate 90 degrees clockwise
    #Navigation.goer_no_gyro(tank, -245, -15)

    colorful_flipper.on_for_rotations(8, 0.125)
    sleep(1)
    colorful_flipper.on_for_rotations(5, -0.125)

    tank.turn_degrees(5, 90)
    Navigation.goer_no_gyro(tank, 65, 40)


if __name__ == "__main__":
    time1 = time()
    tv()
    windmill()
    toystory3()

    time2 = time()
    init.debug_print(time2-time1)
