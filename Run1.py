#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep
import Navigation

def Run():
    tank = Navigation.tank_init()
    flipper=LargeMotor(OUTPUT_C)

    #FlameThingy(tank, flipper)
    #Boxythingy(tank, flipper)
    #MoveyThingy(tank, flipper)
    HighFiveyThingy(tank, flipper)

def FlameThingy(tank, flipper):

    # ex: tank.on_for_rotations(30, 30, 1) #forward (left speed(rpm), right speed(rpm), rotations)
    # ex: tank.turn_degrees(20, 45, True, .1) #turn(speed, degrees, brake after turning, accuracy)

    # ex: Navigation.distance_goer(tank, 30, 30, 7) #move better(tank, distancecm, speed, angle currently at)
    # ex: Navigation.gyro_check(tank, 1, 7) #ACCURATE TURNING(tank, speed, degrees)

    Navigation.distance_goer(tank, 22, -20, 0)
    Navigation.gyro_check(tank,5,22)
    Navigation.distance_goer(tank, 15,-20, 22)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.distance_goer(tank, 18,-10,0)
    sleep(.5)
    Navigation.gyro_check(tank,5,0)
    Navigation.goer_no_gyro(tank, 5, -10)
    Navigation.gyro_check(tank,5,0)


    for x in range(3):
        flipper.on_for_rotations(-5,0.15)
        sleep(0.5)
        flipper.on_for_rotations(5,0.15)
    Navigation.goer_no_gyro(tank, 5, 10)
   # Navigation.distance_goer(tank,5,20,0)
    #Navigation.gyro_check(tank,5,22)
    #Navigation.distance_goer(tank,5,20,22)
    #Navigation.gyro_check(tank,5,-22)
    #flipper.on_for_rotation(-5,0.15)

def Boxythingy(tank, flipper):
    Navigation.gyro_check(tank, 5, 22)
    Navigation.goer_no_gyro(tank, 8.5, -10)
    Navigation.gyro_check(tank, 5, 0)
    flipper.on_for_rotations(-5, 0.15)
    Navigation.distance_goer(tank, 14, -10, 0)
    Navigation.gyro_check(tank, 5, 0)
    flipper.on_for_rotations(5, 0.15)
    Navigation.goer_no_gyro(tank, 7, 5)
    sleep(1)
    flipper.on_for_rotations(-5, 0.15)


def MoveyThingy(tank, flipper):
    Navigation.goer_no_gyro(tank, 7, 5)
    Navigation.gyro_check(tank, 5, 28)
    Navigation.distance_goer(tank, 25, -10, 28)
    sleep(1)

    Navigation.gyro_check(tank, 5, 60)
    Navigation.distance_goer(tank, 20, -10, 60)

def HighFiveyThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.gyro_check(tank, 5, 50)
    Navigation.distance_goer(tank, 40, -10, 50)
    flipper.on_for
    Navigation.gyro_check(tank, 5, -60)





if __name__ == "__main__":
    Run()

