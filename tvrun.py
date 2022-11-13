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
    #tank.turn_degrees(10, 90)
    #colorful_flipper.on_for_rotations(5, 0.3)
    time1 = time()
    #Tv run 1.3
    Navigation.goer_no_gyro(tank, 31.5, -40)
    #tank.on_for_rotations(-20, -20, 1)

    #Go back from
    Navigation.goer_no_gyro(tank, 7, 20)

    #Turn left OG val -45
    Navigation.gyro_check(tank, 5, -47)
    #tank.turn_degrees(10, -30, True, 0.1)

    #Lift flippy
    #colorful_flipper.on_for_rotations(10, -0.25)

    #Pause
    #sleep(2)

    #Parallel to windmill go
    Navigation.goer_no_gyro(tank, 38, -20)

    #Turn almost all the way
    Navigation.gyro_check(tank, 5, 40)

    #NEW code go back
    #Navigation.goer_no_gyro(tank, 2, 20)

    #Lower flipper
    colorful_flipper.on_for_rotations(5, 0.4)

    #Turns all the way OG used to not be commented: 👇
    tank.turn_degrees(5, 2, True, 0.1)
    #tank.turn_degrees(20, 1)
    init.debug_print(tank.gyro.angle)


    time2 = time()
    init.debug_print(time2-time1)
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
    sleep(0.5)

    #Push windmill OG val -15, 0.4 rotations
    time1 = time()
    for x in range(3):
        tank.on_for_rotations(-7, -7, 0.22)
        tank.on_for_rotations(7, 7, 0.22)

def toystory3():

    colorful_flipper = LargeMotor(OUTPUT_C)
    tank = Navigation.tank_init()

    Navigation.goer_no_gyro(tank, 6, 20)

    #Lift colorful flipper Og val 5, -0.25
    sleep(1)
    colorful_flipper.on_for_rotations(5, -0.25)
    '''
    colorful_flipper.on_for_rotations(20, -0.15)
    #sleep(0.25)
    colorful_flipper.on_for_rotations(10, -0.075)
    #sleep(0.25)
    colorful_flipper.on_for_rotations(5, -0.06)
    #sleep(0.25) OG--0.035
    '''

    #Move forward
    tank.on_for_rotations(-20, -20, 0.32)

    #Rotate 90 degrees clockwise
    tank.turn_degrees(10, 90)
    tank.on_for_rotations(10, 10, 0.3)
    tank.turn_degrees(10, 65)

    tank.on_for_rotations(10, 10, 0.1)
    tank.turn_degrees(10, 4)

    #Move forward tiny bit OG val 0.1, then 0.3 DUMP THINGY INTO TOY STORY
    tank.on_for_rotations(-20, -20, 0.3)

#NEW NEW NEW NEW
    #NEW code turn to right a little bit
    tank.turn_degrees(10, 14)

    #Move it down Og val 25, 0.125
    #colorful_flipper.on_for_rotations(15, 0.125)
    Navigation.goer_no_gyro(tank, 22, 15)

    sleep(1)

    colorful_flipper.on_for_rotations(25, 0.125)
    sleep(1)
    return

    #Launch the energy unit
    tank.turn_degrees(70, -6)

    #tank.on_for_rotations(15, 15, 0.5) This is OG val

    return

    #Turn and go back
    tank.on_for_rotations(-20, 20, 0.6)
    tank.on_for_rotations(-20, -20, 2.5)

    time2 = time()
    init.debug_print(time2-time1)
    return

    #Move forward
    tank.on_for_rotations(10, 10, 0.25)
    return

    #Go back

    #Activate mm
    colorful_flipper.on_for_rotations(50, 0.02)
    sleep(0.5)
    #Go towards windmill

    for i in range(3):
        tank.on_for_rotations(-10, -10, 0.41)
        tank.on_for_rotations(10, 10, 0.41)

    return



    #Navigation.distance_goer(tank, 29, 30, 0)
'''
    Navigation.distance_goer(tank, 40, 30, 0)
    sleep(1)
    Navigation.distance_goer(tank, 5, -30, 0)
    sleep(1)
    Navigation.gyro_check(tank, 5, -45)
    Navigation.distance_goer(tank, 40, 30, -45)
    Navigation.gyro_check(tank, 5, 50)
    Navigation.distance_goer(tank, 10, 30, 50)
    for x in range(3):
        Navigation.distance_goer(tank, 30, 30, 50)
        sleep(1)
        Navigation.distance_goer(tank, 15, -30, 50)
        Navigation.gyro_check(tank, 5, 50)
'''
if __name__ == "__main__":
    time1 = time()
    tv()
    windmill()
    toystory3()
    time2 = time()
    init.debug_print(time2-time1)
