#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep, time
import Navigation
import threading
import init


def tv(tank, colorful_flipper):


    #Lower flipper
    colorful_flipper.on_for_rotations(10, 0.4)

    #Tv run 1.3
    #OG distance = 14
    Navigation.goer_no_gyro(tank, 13.25, -30)
    # ^ speed used to be 30
    # ^ distance used to be 12.25
    sleep(0.5)

    #Lift flipper
    colorful_flipper.on_for_rotations(-10, 0.4)
    Navigation.goer_no_gyro(tank, 1, 20) #speed used to be 10
    #Pranav says hi
    #Turn left OG val -45
    Navigation.gyro_check(tank, 7, -42) #speed used to be 7
    #init.debug_print("Should be -42:", tank.gyro.angle)



    #Parallel to windmill go
    #Navigation.goer_no_gyro(tank, 53, -35)
    Navigation.distance_goer(tank, 53, -35, -47) #speed used to be -30

    #added for testing
    colorful_flipper.on_for_rotations(10, 0.4) #speed used to be 10
    Navigation.goer_no_gyro(tank, 15, -25)
    colorful_flipper.on_for_rotations(10, -0.4) #speed used to be 7
    Navigation.goer_no_gyro(tank, 15, 25)


    #Turn almost all the way
    Navigation.gyro_check(tank, 7, 40) #speed used to be 7
    #init.debug_print("Should be 40:", tank.gyro.angle)

    #Go forward from
    #Lower flipper
    colorful_flipper.on_for_rotations(10, 0.4) #speed used to be 5


    #Turns all the way OG used to not be commented: 👇
    #4tank.turn_degrees(5, 2, True, 0.1)
    #tank.turn_degrees(20, 1)
    #Put colorful flipper down


def windmill(tank, colorful_flipper):
    #Push windmill OG val -15, 0.4 rotations
    time1 = time()
    for x in range(4):
        tank.on_for_rotations(-10, -10, 0.27)
        tank.on_for_rotations(7, 7, 0.24)

def toystory3(tank, colorful_flipper):


   # Navigation.goer_no_gyro(tank, 5.5, 20)

    #Lift colorful flipper Og val 5, -0.25
    Navigation.gyro_check(tank, 7, 20) #speed used to be 7
    #init.debug_print("Should be -20:", tank.gyro.angle)
    colorful_flipper.on_for_rotations(7, -0.35)

    sleep(0.25)
    Navigation.gyro_check(tank, 7, -100) #speed used to be 5
    Navigation.goer_no_gyro(tank, 3, 25) #speed used to be 20
    Navigation.gyro_check(tank, 7, -125) #speed used to be 5
    # ^ used to be -165
    #init.debug_print("Should be -165:", tank.gyro.angle)
    #Navigation.goer_no_gyro(tank, 3, 20)

    #Rotate 90 degrees clockwise
    #Navigation.goer_no_gyro(tank, -245, -15)

    colorful_flipper.on_for_rotations(8, 0.125)

    sleep(0.5)
    colorful_flipper.on_for_rotations(5, -0.2)

    #Navigation.goer_no_gyro(tank, 2, -15)
    #used to not be here ^

    #needs to be 65 if running vroomycar
    tank.turn_degrees(10, 93)
    # ^ used to be 93
    # ^ used to be 90

    #Originally not commented(moved into vroomycar)
    Navigation.goer_no_gyro(tank, 65, 40)
    tank.turn_degrees(20, -45)
    Navigation.goer_no_gyro(tank, 10, 30)

'''
def vroomycar():

    colorful_flipper = LargeMotor(OUTPUT_C)
    tank = Navigation.tank_init()

    colorful_flipper.on_for_rotations(5, 0.35)
    Navigation.goer_no_gyro(tank, 16, -20)
    tank.turn_degrees(10, 15)
    colorful_flipper.on_for_rotations(5, -0.15)
    colorful_flipper.on_for_rotations(5, 0.15)
    sleep(0.5)
    tank.turn_degrees(5, -5)

    #coming back to home
    Navigation.goer_no_gyro(tank, 75, 35)
    colorful_flipper.on_for_rotations(10, -0.35)

'''


if __name__ == "__main__":
    time1 = time()
    colorful_flipper=LargeMotor(OUTPUT_C)
    tank = Navigation.tank_init()

    tv(tank, colorful_flipper)
    windmill(tank, colorful_flipper)
    toystory3(tank, colorful_flipper)
    #vroomycar()

    time2 = time()
    init.debug_print(time2-time1)
