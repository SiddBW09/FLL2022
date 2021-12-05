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
    sleep(5)


    #Blue thing mission
    Navigation.distance_to_object(tank, 30, "Forward", 20)

    #Complete blue cargo thing mission
    tank.turn_degrees(50, -45, True, 1)
    sleep(2)
    degrees_to_turn = 0 - tank.gyro.angle
    tank.turn_degrees(5, degrees_to_turn, True, 1)
    sleep(0.5)



    Navigation.distance_to_object(tank, 30, "Forward", 10)

    tank.turn_degrees(10, 35, True, 1)


    #Number of degrees need to turn to SwitchE
    degrees_to_turn = 35- tank.gyro.angle
    tank.turn_degrees(5, degrees_to_turn, True, 1)



    #Go to SwitchE
    Navigation.distance_to_object(tank, 25, "Forward", 10)

    #Turn right
    Claw.claw_open(100)
    sleep(1)
    tank.turn_degrees(10, 15, True, 1)
    init.debug_print(tank.gyro.angle)

    Navigation.distance_to_object(tank, 11, "Forward", 10)

    #OG value 5
    tank.turn_degrees(10, 5, True, 1)
    #Navigation.gyro_check(tank, 35, 45)
    Claw.claw_close(100)



    #Do SwitchE mission
    lift.on_for_rotations(10, -1)


     #try again to please Coach Hari
    Claw.claw_open(100)
    tank.turn_degrees(10, 4, True, 1)
    lift.on_for_rotations(10, 1)
    Claw.claw_close(100)
    lift.on_for_rotations(10, -1)


    #Go back to orange planey
    tank.turn_degrees(25, -5, True, 1)
    Navigation.distance_to_object(tank, 12, "Backward", 10)
    tank.turn_degrees(25, -15, True, 1)
    Navigation.distance_to_object(tank, 20, "Backward", 10)
    lift.on_for_rotations(35, -1)

    #Turn to Green thing
    tank.turn_degrees(20, -45, True, 1)

    #Complete Green mission
    Navigation.distance_to_object(tank, 7, "Forward", 10)
    lift.on_for_rotations(35, 3)
    Claw.claw_close(100)
    lift.on_for_rotations(35, 0.3)
    tank.turn_degrees(25, -5, True, 1)
    Navigation.distance_to_object(tank, 20, "Forward", 10)

    #Go back
    Navigation.distance_to_object(tank, 10, "Backward", 10)
    return

    tank.turn_degrees(15, 55, True, 1)
    Navigation.distance_to_object(tank, 9, "Forward", 10)
    lift.on_for_rotations(10, 1)


    return

    #Go back from SwitchE
    tank.turn_degrees(10, -5, True, 1)
    tank.turn_degrees(10, -10, True, 1)
    Navigation.distance_to_object(tank, 25, "Backward", 10)




    return



#Execute Northide Missions
if __name__ == "__main__":
    #Sahana_And_Pranav_Code()
    Coachie_Code()
