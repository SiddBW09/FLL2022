#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep, time
import Navigation, init
from threading import Thread
from ev3dev2.sound import Sound

'''Function that calls all the misson code for this run'''
def PlatformRun(tank, flipper, sweeper):
    tank.gyro.reset()

    OilandHydro(tank, flipper, sweeper)

    Sweeper(tank, flipper, sweeper)

    GrabNGo(tank, flipper, sweeper)

'''Does Oil Platform with the flipper and does Hydroelectric Dam with sweeper'''
def OilandHydro(tank, flipper, sweeper):

    #Flip flipper down, and go to Oil platform
    Navigation.gyro_check(tank, 7, 45)
    Navigation.distance_goer(tank, 8, -20, 45)
    Navigation.gyro_check(tank, 7, 0)
    flipper.reset()
    flipper.on_for_rotations(30, 0.45)
    Navigation.distance_goer(tank, 43, -30, 0)

    #Do oil platform and hydro dam at once
    sweeper.on_for_rotations(25, 0.2)

    for x in range(3):
        flipper.on_for_rotations(-15, 0.12)
        sweeper.on_for_rotations(-15, 0.2)
        flipper.on_for_rotations(15, 0.12)
        sweeper.on_for_rotations(25, 0.2)

    sweeper.on_for_rotations(-20, 0.1)

    #Turn and go to Solar Farm
    Navigation.gyro_check(tank, 5, 45)
    Navigation.distance_goer(tank, 36, -35, 45)
    Navigation.gyro_check(tank, 7, 90)

'''Sweep the energy units in the Solar Farm in one place'''
def Sweeper(tank, flipper, sweeper):

    #Move back and move flipper and sweeper down to prepare for sweeping
    Navigation.distance_goer(tank, 8, 25, 90)
    Navigation.gyro_check(tank, 5, 90)
    flipper.on_for_rotations(-20, 0.35)
    sweeper.on_for_rotations(-20, 0.5)

    #Sweep the energy units
    Navigation.distance_goer(tank, 30, -35, 90)

'''Collect energy units from Solar Farm, do Smart Grid, and collect water units'''
def GrabNGo(tank, flipper, sweeper):

    #Prepare for Smart Grid
    sweeper.on_for_rotations(20, 0.35)
    Navigation.gyro_check(tank, 9, 180)
    sweeper.on_for_rotations(15, -0.1)

    #Collect units in the back and do Smart Grid
    Navigation.distance_goer(tank, 26, 25, 180)

    #Prepare for collecting water units
    flipper.on_for_rotations(20, 0.38)

    #Grab water units
    Navigation.distance_goer(tank, 19, -25, 185)

    #Go to Left Home
    tank.turn_degrees(20, -25)
    Navigation.gyro_check(tank, 5, 160)
    Navigation.distance_goer(tank, 50, -30, 160)
    Navigation.gyro_check(tank, 10, 255)
    Navigation.goer_no_gyro(tank, 40,-20)
    Navigation.goer_no_gyro(tank, 40,-50)

    #Prepare for next run
    flipper.on_for_rotations(-40, 0.7)
    sweeper.on_for_rotations(15, 0.145)

'''Dumps energy units into Energy Storage, grabs tray, and grabs Oil Platform truck'''
def EnergyStorage(tank, flipper, sweeper):

    #Testing
    Navigation.gyro_check(tank, 10, 45)
    Navigation.distance_goer(tank, 17, -20, 45)
    Navigation.gyro_check(tank, 10, 0)
    Navigation.distance_goer(tank, 60, -30, 0)

    '''
    #Align the robot to the Energy Storage
    Navigation.distance_goer(tank, 5, -20, 0)
    Navigation.gyro_check(tank, 5, 22)
    Navigation.distance_goer(tank, 14, -20, 22)
    Navigation.gyro_check(tank, 5, 0)

    #Go to Energy Storage and flip energy units in to the storage bin
    Navigation.distance_goer(tank, 60, -35, 0)
    '''
    flipper.reset()
    flipper.on_for_rotations(-40, 0.45)

    #Grab onto tray
    Navigation.distance_goer(tank, 10, 10, 0)
    flipper.on_for_degrees(25, 83)

    #Go to home
    Navigation.distance_goer(tank, 66, 60, 3)
    tank.turn_degrees(40, -85)
    Navigation.goer_no_gyro(tank, 10, -40)
    flipper.on_for_rotations(-40, 0.95)

    return

    '''Code necessary for grabbing the truck in the Oil Platform'''

    #Move to the truck
    Navigation.gyro_check(tank, 15, -35)
    flipper.on_for_rotations(20, 0.41)
    Navigation.distance_goer(tank, 38, -25, -35)

    #Grab the truck
    tank.on_for_rotations(10, 45, 1.5)
    tank.on_for_rotations(-34, -35, 0.5)

    #Move to home
    Navigation.goer_no_gyro(tank, 4, -30)
    Navigation.distance_goer(tank, 35, 35, 0)
    Navigation.gyro_check(tank, 5, 22)
    Navigation.distance_goer(tank, 45, 40, 22)
    flipper.on_for_rotations(-25, 0.21)


if __name__ == "__main__":
    tank = Navigation.tank_init()
    flipper = LargeMotor(OUTPUT_C)
    sweeper = MediumMotor(OUTPUT_D)
    time1 = time()

    PlatformRun(tank, flipper, sweeper)
    #EnergyStorage(tank, flipper, sweeper)

    init.debug_print(time()-time1)
