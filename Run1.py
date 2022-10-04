#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep
import Navigation

def North():
    tank = Navigation.tank_init()
    flipper=LargeMotor(OUTPUT_C)

    # ex: tank.on_for_rotations(30, 30, 1) #forward (left speed(rpm), right speed(rpm), rotations)
    # ex: tank.turn_degrees(20, 45, True, .1) #turn(speed, degrees, brake after turning, accuracy)

    # ex: Navigation.distance_goer(tank, 30, 30, 7) #move better(tank, distancecm, speed, angle currently at)
    # ex: Navigation.gyro_check(tank, 1, 7) #ACCURATE TURNING(tank, speed, degrees)

    Navigation.distance_goer(tank, 22, -30, 0)
    Navigation.gyro_check(tank,5,22)
    Navigation.distance_goer(tank,19,-30, 22)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.distance_goer(tank, 15,-10,0)

    for x in range(3):
        Navigation.distance_goer(tank, 3,-10,0)
        flipper.on_for_rotations(-5,0.15)
        Navigation.gyro_check(tank, 5, 0)
        sleep(0.5)
        flipper.on_for_rotations(5,0.15)
        Navigation.gyro_check(tank, 5, 0)
        Navigation.distance_goer(tank,2,10,0)



if __name__ == "__main__":
    North()
