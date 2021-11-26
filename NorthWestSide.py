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
import claw

def Sahana_And_Pranav_Code():
    tank = Navigation.tank_init()
    lift = MediumMotor(OUTPUT_D)
    Claw = claw.Claw()



    #Go to Switch-E
    Navigation.distance_to_object(tank, 55, "Forward", 20)
    Navigation.turn_degrees(tank, 50, "Right")
    Navigation.distance_to_object(tank, 40.5, "Forward", 20)
    Claw.claw_open(100)
    Claw.claw_close(100)
    lift.on_for_rotations(-20, 1.5)
    Navigation.distance_to_object(tank, 40.5, "Backward", 15)
    Navigation.turn_degrees(tank, 50, "Left")
    Navigation.distance_to_object(tank, 6.5, "Forward", 20)
    sleep(1)
    lift.on_for_rotations(-10, 1)


    # init.debug_print(rt_large)
    # init.debug_print(lt_large)





#Execute Northide Missions
if __name__ == "__main__":
    Sahana_And_Pranav_Code()
