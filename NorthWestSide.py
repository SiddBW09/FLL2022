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
import Navigation
import init
import claw

def Coachie_Code():
    tank = Navigation.tank_init()
    lift = MediumMotor(OUTPUT_D)
    Claw = claw.Claw()
    tank.gyro.reset()


    # Blue thing mission
    Navigation.distance_to_object(tank, 28, "Forward", 20)

    tank.on_for_rotations(0, 10, 0.8)
    tank.on_for_rotations(0, -10, 0.8)
    Navigation.gyro_check(tank, 5, 0)
    init.debug_print(tank.gyro.angle)

    Navigation.distance_to_object(tank, 25, "Forward", 10)

    tank.turn_degrees(10, 35, True, 1)


    Navigation.gyro_check(tank, 5, 35)


    #Go to SwitchE
    Navigation.distance_to_object(tank, 35, "Forward", 10)

    Claw.claw_open(100)

    sleep(2)
    tank.turn_degrees(10, 15, True, 1)
    Navigation.distance_to_object(tank, 8, "Forward", 10)

    #OG value 5
    tank.turn_degrees(10, 8, True, 1)
    Claw.claw_close(100)



    #Do SwitchE mission
    lift.on_for_rotations(-30, 2)

    return

    Claw.claw_close(100)

    #Go back to orange planey
    tank.turn_degrees(5, -5, True, 1)
    Navigation.distance_to_object(tank, 8, "Backward", 10)
    tank.turn_degrees(5, -15, True, 1)
    Navigation.distance_to_object(tank, 25, "Backward", 10)


    #Turn to Green thing
    tank.turn_degrees(20, -60, True, 1)
    Navigation.gyro_check(tank, 5, -25)

    #Complete Green mission
    Navigation.distance_to_object(tank, 9, "Forward", 10)
    Claw.claw_close(100)
    lift.on_for_rotations(35, 1)
    return



    return



    return



#Execute Northide Missions
if __name__ == "__main__":
    #Sahana_And_Pranav_Code()
    Coachie_Code()
