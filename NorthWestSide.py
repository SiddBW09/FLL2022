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



    #Lift up at start
    lift.on_for_rotations(-10, 0.1)

    # Blue thing mission
    Claw.claw_open(100)

    #Go to blue mission thing
    Navigation.distance_to_object(tank, 30, "Forward", 20)

    tank.on_for_rotations(0, 10, 0.8)
    tank.on_for_rotations(0, -10, 0.8)
    Navigation.gyro_check(tank, 5, 0)


    Navigation.distance_to_object(tank, 27, "Forward", 10)

    #Turn and Go to SwitchE
    tank.turn_degrees(10, 40, True, 1)
    Navigation.gyro_check(tank, 5, 40)
    Navigation.distance_to_object(tank, 27, "Forward", 10)
    Claw.claw_open(100)

    return

    #Lift
    lift.on_for_rotations(-100, 1)
    tank.turn_degrees(10, 9, True, 1)

    Navigation.distance_to_object(tank, 10, "Forward", 10)
    Navigation.gyro_check(tank, 10, 60)

    lift.on_for_rotations(100, 1)
    Claw.claw_close(100)
    lift.on_for_rotations(-30, 6)
    Claw.claw_close(100)
    Navigation.gyro_check(tank, 5, 40)


    #Go back to home (OG val 50)
    Navigation.distance_to_object(tank, 60, "Backward", 10)
    Navigation.gyro_check(tank, 5, 40)

    #Turn to 0
    tank.turn_degrees(10, -35, True, 1)
    Navigation.gyro_check(tank, 5, 0)


    #GO at 0
    Navigation.distance_to_object(tank, 29, "Forward", 10)

    #Turn perpendicular to Cargo Plane
    tank.turn_degrees(10, 34, True, 1)
    Navigation.gyro_check(tank, 5, 36)

    lift.on_for_rotations(100, 2)
    sleep(1)
    lift.on_for_rotations(100, 4, brake = True)
    sleep(1)


    lift.on_for_rotations(-100, 6)
    tank.turn_degrees(10, 20, True, 1)
    Navigation.distance_to_object(tank, 10, "Forward")
    lift.on_for_rotations(100, 6)
    Navigation.distance_to_object(tank, 12, "Backward")
    lift.on_for_rotations(100, 6)


    return




#Execute Northide Missions
if __name__ == "__main__":
    #Sahana_And_Pranav_Code()
    Coachie_Code()
