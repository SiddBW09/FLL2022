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

def Coach_Code(tank, lift, Claw):
    #tank = Navigation.tank_init()
    #lift = MediumMotor(OUTPUT_D)
    #Claw = claw.Claw()
    tank.gyro.reset()
    start_time = time.time()

    #Lift up at start
    lift.on_for_rotations(10, 3)
    lift.reset()


    #Go to blue mission thing
    Navigation.distance_goer(tank, 30, 32, 0)
    tank.on_for_rotations(0, 30, 0.8)
    tank.on_for_rotations(0, -30, 0.8)
    Navigation.gyro_check(tank, 5, 0)


    #Go forward more
    
    Navigation.distance_goer(tank, 28, 34, 0)


    #Turn and Go to SwitchE
    tank.turn_degrees(10, 40, True, 1)
    Navigation.gyro_check(tank, 5, 40)


    Navigation.distance_goer(tank, 15, 30, 40)
    Navigation.gyro_check(tank, 5, 40)
    Navigation.distance_to_object(tank, 12, "Forward")
    


    Navigation.distance_to_object(tank, 6.5, "Forward", 10)
    Navigation.gyro_check(tank, 10, 50)

    lift.on_for_rotations(-70, 5)



    #Go back to home
    #OG val=- -30, 37
    Navigation.new_move_incm(tank, -30, 39)
    Navigation.gyro_check(tank, 5, 40)

    #Turn to 0
    tank.turn_degrees(10, -20, True, 1)
    sleep(1)

    lift.reset()
    lift.on_for_rotations(60, 8)
    lift.reset()
    lift.on_for_rotations(-60, 0.6)
    lift.reset()

    lift.on_for_rotations(60, 8)
    lift.reset()
    lift.on_for_rotations(60, -8)

    #Do green cargo mission
    #OG val 3, then 2 then 1.4
    Navigation.distance_to_object(tank, 1.4, "Forward")

    #Og val= .35 then .225
    tank.on_for_rotations(10, 0, .2)

    #Go forward and grab grey cargo
    Navigation.distance_to_object(tank, 11, "Forward")
    lift.on_for_rotations(60, 8)

    #Go back to put grey cargo in grey circle
    Navigation.distance_to_object(tank, 11, "Backward")
    lift.on_for_rotations(60, -8)
    sleep(0.5)

    '''endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))'''

    #return
    Navigation.distance_goer(tank, 33, -25, 40)
    tank.turn_degrees(10, -30, True, 1)

    #init.debug_print(int(time.time()-start_time))
    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))
    lift.reset()
    Claw.claw.reset()
    return




#Execute Northide Missions
if __name__ == "__main__":
    Coach_Code(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())