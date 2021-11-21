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
    tank = MoveTank(OUTPUT_D, OUTPUT_A)
   
    claw = MediumMotor(OUTPUT_C)

    lift = MediumMotor(OUTPUT_B)

    # Init Color Sensors
    colorRight = ColorSensor(INPUT_2)
    colorLeft = ColorSensor(INPUT_3)


    # init Gyro Sensor
    tank.gyro = GyroSensor(INPUT_1)
    tank.gyro.mode='GYRO-ANG'
    tank.gyro.reset() 

    tank.turn_left(20, 90)
   
    Navigation.Line_Following(tank, colorLeft, colorRight, 18)


#Execute Northide Missions
if __name__ == "__main__":
    Sahana_And_Pranav_Code()
