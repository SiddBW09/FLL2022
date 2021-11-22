#!/usr/bin/env python3

'''
Imports:
'''
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B,MoveTank, SpeedPercent, follow_for_ms, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import Navigation
from time import sleep
from ev3dev2.motor import OUTPUT_B, MediumMotor
import init

def Sahana_And_Pranav_Code():
    tank = Navigation.tank_init()

    init.debug_print("Inital Degrees: " + str(tank.gyro.angle))
    Navigation.turn_degrees(tank, 90, "Left")
    init.debug_print("After Degrees: " + str(tank.gyro.angle))


#Execute Northide Missions
if __name__ == "__main__":
    Sahana_And_Pranav_Code()
