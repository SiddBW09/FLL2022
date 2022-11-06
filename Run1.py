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
    Boxythingy(tank, flipper)
    MoveyThingy(tank, flipper)
    # HighFiveyThingy(tank, flipper)
    # CaryThingy(tank, flipper)

def FlameThingy(tank, flipper):

    # ex: tank.on_for_rotations(30, 30, 1) #forward (left speed(rpm), right speed(rpm), rotations)
    # ex: tank.turn_degrees(20, 45, True, .1) #turn(speed, degrees, brake after turning, accuracy)

    # ex: Navigation.distance_goer(tank, 30, 30, 7) #move better(tank, distancecm, speed, angle currently at)
    # ex: Navigation.gyro_check(tank, 1, 7) #ACCURATE TURNING(tank, speed, degrees)

    Navigation.distance_goer(tank, 22, -20, 0)
    sleep(.5)
    Navigation.gyro_check(tank,5,22)
    Navigation.distance_goer(tank, 21 ,-20, 22)
    sleep(0.5)
    Navigation.gyro_check(tank, 5, 0)
    sleep(0.5)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.distance_goer(tank, 17, -10, 0)
    sleep(0.5)
    Navigation.gyro_check(tank,1,0)
    sleep(0.5)
    Navigation.gyro_check(tank,1,0)
    sleep(1)


    for x in range(0, 3):
        flipper.on_for_rotations(-5, 0.15)
        sleep(1)
        flipper.on_for_rotations(5, 0.15)
        sleep(1)

    Navigation.goer_no_gyro(tank, 5, 10)
    Navigation.gyro_check(tank,5,22)
    Navigation.goer_no_gyro(tank, 9, -10)
    sleep(1)
    Navigation.gyro_check(tank, 3, 0)


def Boxythingy(tank, flipper):
    tank.gyro.reset()
    flipper.on_for_rotations(-5, 0.15)
    Navigation.goer_no_gyro(tank, 14.5, -10)
    sleep(0.5)
    Navigation.gyro_check(tank, 5, 0)
    flipper.on_for_rotations(5, 0.15)
    Navigation.distance_goer(tank, 6, 10, 0)
    flipper.on_for_rotations(-5, 0.15)
    sleep(1)
    Navigation.gyro_check(tank, 5, 0)



def MoveyThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.gyro_check(tank, 5, 28)
    flipper.on_for_rotations(5, 0.15)
    Navigation.distance_goer(tank, 25, -10, 28)
    sleep(1)
    Navigation.gyro_check(tank, 5, 70)
    Navigation.distance_goer(tank, 20, -10, 70)
    Navigation.gyro_check(tank, 5, 90)

def HighFiveyThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.gyro_check(tank, 5, 22)
    Navigation.distance_goer(tank, 35, -25, 22)
    flipper.on_for_rotations(-5, 0.2)
    Navigation.gyro_check(tank, 5, -90)
    flipper.on_for_rotations(5, 0.2)
    Navigation.goer_no_gyro(tank, 7, 10)
    flipper.on_for_rotations(-5, 0.2)
    Navigation.gyro_check(tank, 5, 0)
    flipper.on_for_rotations(5, 0.2)

def CaryThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.goer_no_gyro(tank,10, -10)
    Navigation.gyro_check(tank, 5, -74)
    sleep(1)
    Navigation.distance_goer(tank, 18, -10, -74)
    flipper.on_for_rotations(-25, 0.5)







if __name__ == "__main__":
    Run()

