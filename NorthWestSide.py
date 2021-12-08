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
import time
from ev3dev2.motor import OUTPUT_B, MediumMotor
import Navigation
import init
import claw

def Coachie_Code():
    tank = Navigation.tank_init()
    lift = MediumMotor(OUTPUT_D)
    Claw = claw.Claw()
    tank.gyro.reset()
    start_time = time.time()

    '''
    Testy Test test
    for x in range(0, 4):
        tank.turn_degrees(10, -90, True, 1)
        Navigation.gyro_check(tank, 10, -90)
        init.debug_print(tank.gyro.angle)
    '''

    lift.on_for_rotations(-10, 0.1)
    #Lift up at start

    # Blue thing mission
    Claw.claw_open(100)

    #Go to blue mission thing
    Navigation.distance_to_object(tank, 30, "Forward", 20)

    tank.on_for_rotations(0, 10, 0.8)
    tank.on_for_rotations(0, -10, 0.8)
    Navigation.gyro_check(tank, 5, 0)
    init.debug_print(tank.gyro.angle)

    Navigation.distance_to_object(tank, 25, "Forward", 10)

    #Do the blue mission thing
    tank.turn_degrees(10, 35, True, 1)


    Navigation.gyro_check(tank, 5, 35)

    #Go to SwitchE
    Navigation.distance_to_object(tank, 35, "Forward", 10)

    Claw.claw_open(30)

    tank.turn_degrees(10, 15, True, 1)
    Navigation.distance_to_object(tank, 8, "Forward", 10)

    #OG value 5
    Navigation.gyro_check(tank, 5, 65)
    Claw.claw.on_for_rotations(50, 1)


    #Do SwitchE mission
    lift.on_for_rotations(-50, 3)
    Claw.claw_close(100)


    #Go back to home
    tank.turn_degrees(5, -5, True, 1)
    Navigation.distance_to_object(tank, 8, "Backward", 10)
    tank.turn_degrees(5, -15, True, 1)
    Navigation.distance_to_object(tank, 60, "Backward", 10)
    Navigation.gyro_check(tank, 5, 35)

    #Turn to 0
    tank.turn_degrees(10, -35, True, 1)
    Navigation.gyro_check(tank, 5, 0)

    #Go at 0
    Navigation.distance_to_object(tank, 26, "Forward", 10)

    #Turn to perpendicular and approach
    tank.turn_degrees(10, 47, True, 1)
    #Navigation.distance_to_object(tank, 10, "Forward", 10)

    #Go to Cargo Plane and do mission
    Navigation.distance_to_object(tank, 6, "Forward", 10)
    Claw.claw_open(100)
    lift.on_for_rotations(100, 6)
    Claw.claw_close(100)
    tank.turn_degrees(10, 27)
    Navigation.gyro_check(tank, 10, 27)
    lift.on_for_rotations(-30, 6)
    Claw.claw_open(100)
    Navigation.distance_to_object(tank, 5, "Forward", 10)
    lift.on_for_rotations(30, 6)


#Execute Northide Missions
if __name__ == "__main__":
    #Sahana_And_Pranav_Code()
    Coachie_Code()
