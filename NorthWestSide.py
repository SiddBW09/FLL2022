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

def Coachie_Code():
    tank = Navigation.tank_init()
    lift = MediumMotor(OUTPUT_D)
    Claw = claw.Claw()
    tank.gyro.reset()
    sleep(5)

    #Forkytestytest (Keep this code please)
    lift.on_for_rotations(100, 2)
    tank.on_for_rotations(25, 25, 0.2)
    tank.turn_degrees(25, -25, True, 1)
    return

    #Blue thing mission
    Navigation.distance_to_object(tank, 30, "Forward", 20)

    #Complete blue cargo thing mission
    tank.turn_degrees(50, -45, True, 1)
    sleep(2)
    degrees_to_turn = 0 - tank.gyro.angle
    tank.turn_degrees(10, degrees_to_turn, True, 1)
    sleep(0.5)



    Navigation.distance_to_object(tank, 30, "Forward", 10)

    tank.turn_degrees(10, 40, True, 1)

    #Number of degrees need to turn to SwitchE
    degrees_to_turn = 45- tank.gyro.angle
    tank.turn_degrees(5, degrees_to_turn, True, 1)

    init.debug_print(tank.gyro.angle)

    #Go to SwitchE
    Navigation.distance_to_object(tank, 25, "Forward", 10)

    #Turn right
    Claw.claw_open(100)
    init.debug_print(tank.gyro.angle)
    sleep(1)
    tank.turn_degrees(10, 10, True, 1)
    init.debug_print(tank.gyro.angle)

    Navigation.distance_to_object(tank, 11, "Forward", 10)

    tank.turn_degrees(10, 5, True, 1)

    Claw.claw_close(100)



    #Do SwitchE mission
    lift.on_for_rotations(10, -1)

    return

    #Go back from SwitchE
    tank.turn_degrees(10, -5, True, 1)
    tank.turn_degrees(10, -10, True, 1)
    Navigation.distance_to_object(tank, 25, "Backward", 10)

    #Turn right to Airplane
    tank.turn_degrees(10, 45, True, 1)

    tank.turn_degrees(10, -3, True, 1)
    Navigation.distance_to_object(tank, 5, "Forward", 5)
    Claw.claw_open(100)
    sleep(0.5)
    lift.on_for_rotations(10, 1)
    Claw.claw_close(100)
    tank.turn_degrees(5, -10, True, 1)
    Claw.claw_open(100)

    return



#Execute Northide Missions
if __name__ == "__main__":
    #Sahana_And_Pranav_Code()
    Coachie_Code()
