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
    #tank.turn_degrees(10, -30, True, 0.1)

    #Lift flippy
    #colorful_flipper.on_for_rotations(10, -0.25)

    #Pause
    #sleep(2)

    #Parallel to windmill go
    Navigation.goer_no_gyro(tank, 53, -30)

    #Turn almost all the way
    Navigation.gyro_check(tank, 5, 40)

    #Go forward from
    Navigation.goer_no_gyro(tank, 2, -15)

    #NEW code go back
    #Navigation.goer_no_gyro(tank, 2, 20)

    #Lower flipper
    colorful_flipper.on_for_rotations(5, 0.4)


    #Turns all the way OG used to not be commented: 👇
    #4tank.turn_degrees(5, 2, True, 0.1)
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
    colorful_flipper.on_for_rotations(7, -0.35)

    sleep(1)
    Navigation.gyro_check(tank, 5, -165)
    Navigation.goer_no_gyro(tank, 3, 20)

    #Rotate 90 degrees clockwise
    #Navigation.goer_no_gyro(tank, -245, -15)

    colorful_flipper.on_for_rotations(5, 0.125)
    init.debug_print(tank.gyro.angle)
    sleep(1)
    colorful_flipper.on_for_rotations(5, -0.125)

    tank.turn_degrees(5, 90)
    Navigation.goer_no_gyro(tank, 65, 40)
    #tank.turn_degrees(10, 180)

    #tank.on_for_rotations(10, 10, 0.3)
    #tank.turn_degrees(10, 65)

    #tank.on_for_rotations(10, 10, 0.1)
    #tank.turn_degrees(10, 4)



    #Move forward tiny bit OG val 0.1, then 0.3 DUMP THINGY INTO TOY STORY
    #tank.on_for_rotations(-20, -20, 0.3)

#NEW NEW NEW NEW
    #NEW code turn to right a little bit
    #tank.turn_degrees(10, 14)

    #Move it down Og val 25, 0.125
    #colorful_flipper.on_for_rotations(15, 0.125)
    #Navigation.goer_no_gyro(tank, 22, -15)

    sleep(1)


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
