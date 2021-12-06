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

    lift.on_for_rotations(-10, 0.1)

    # Blue thing mission
    Claw.claw_open(70)

    #Go to blue mission thing
    Navigation.distance_to_object(tank, 28, "Forward", 20)

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

    tank.turn_degrees(10, 10, True, 1)
    Navigation.distance_to_object(tank, 8, "Forward", 10)

    #OG value 5
    tank.turn_degrees(10, 7, True, 1)
    Claw.claw.on_for_rotations(10, 0.2)


    #Do SwitchE mission
    lift.on_for_rotations(-50, 3)
    Claw.claw_close(100)


    #Go back to home
    tank.turn_degrees(5, -5, True, 1)
    Navigation.distance_to_object(tank, 8, "Backward", 10)
    tank.turn_degrees(5, -15, True, 1)
    Navigation.distance_to_object(tank, 35, "Backward", 15)

    #Turn to Cargo Plane
    turn_degrees = 0 - tank.gyro.angle
    tank.turn_degrees(5, turn_degrees, True, 1)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.distance_to_object(tank, 10, "Forward", 15)

    return
    sleep(1)

    #Do Mission
    Navigation.gyro_check(tank, 10, 0)
    lift.reset()
    lift.on_for_rotations(75, 3)
    sleep(0.5)
    lift.on_for_rotations(-30, 3)
    return
    sleep(0.5)
    tank.turn_degrees(20, 25, True, 1)
    Navigation.gyro_check(tank, 5, 25)
    Claw.claw_open(70)
    lift.on_for_rotations(49, 3)
    Navigation.distance_to_object(tank, 4, "Backward")
    return

    Claw.claw_open(100)
    lift.on_for_rotations(30, 2)
    Claw.claw_close(100)
    Navigation.distance_to_object(tank, 7, "Backward")
    Claw.claw_open(100)
    lift.on_for_rotations(-30, 3, True)
    sleep(0.5)
    return

    #Go Home
    tank.on_for_rotations(-20, -20, 1.5)
    init.debug_print("Time: "+str(time.time()-start_time))

    return



    return



    return



#Execute Northide Missions
if __name__ == "__main__":
    #Sahana_And_Pranav_Code()
    Coachie_Code()
