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

def PraticeCode():
    tank = Navigation.tank_init()
    lift = MediumMotor(OUTPUT_D)
    Claw = claw.Claw()
    tank.gyro.reset()
    start_time = time.time()

    lift.on_for_rotations(10, 1)
    tank.turn_degrees(50, 30, True, 1)
    return

    lift.on_for_rotations(10, -1)
    tank.turn_degrees(10, 20, True, 1)

    return

    #Lift up at start
    lift.on_for_rotations(10, 3)
    lift.reset()


    #Go to blue mission thing
    Navigation.new_move_incm(tank, 32, 30)
    tank.on_for_rotations(0, 30, 0.8)
    tank.on_for_rotations(0, -30, 0.8)
    Navigation.gyro_check(tank, 5, 0)


    #Go forward more
    Navigation.new_move_incm(tank, 34, 28)


    #Turn and Go to SwitchE
    tank.turn_degrees(10, 40, True, 1)
    Navigation.gyro_check(tank, 5, 40)

    Navigation.new_move_incm(tank, 30, 15)
    Navigation.gyro_check(tank, 5, 40)
    lift.on_for_rotations(10, -1)
    tank.turn_degrees(10, 10, True, 1)

    return
    Navigation.distance_to_object(tank, 12, "Forward")


    Navigation.distance_to_object(tank, 6.5, "Forward", 10)
    Navigation.gyro_check(tank, 10, 50)

    lift.on_for_rotations(-70, 5)



    #Go back to home
    Navigation.new_move_incm(tank, -30, 37)
    Navigation.gyro_check(tank, 5, 40)

    #Turn to 0
    tank.turn_degrees(10, -20, True, 1)
    sleep(1)
    #Navigation.gyro_check(tank, 5, 7)


    lift.reset()
    lift.on_for_rotations(60, 8)
    lift.reset()
    lift.on_for_rotations(-60, 0.6)
    lift.reset()

    lift.on_for_rotations(60, 8)
    lift.reset()
    lift.on_for_rotations(60, -8)

    #Do green cargo mission
    #OG val 3
    Navigation.distance_to_object(tank, 2, "Forward")
    tank.on_for_rotations(10, 0, .35)

    #Go forward and grab grey cargo
    Navigation.distance_to_object(tank, 10, "Forward")
    lift.on_for_rotations(60, 8)

    #Go back to put grey cargo in grey circle

    Navigation.distance_to_object(tank, 10, "Backward")
    #Navigation.new_move_incm(tank, -25, 10)
    lift.on_for_rotations(60, -8)
    #Navigation.distance_to_object(tank, 10, "Backward")
    Navigation.new_move_incm(tank, -100, 40)
    tank.turn_degrees(10, -45, True, 1)

    #init.debug_print(int(time.time()-start_time))
    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))
    lift.reset()
    Claw.claw.reset()
    return


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
    Navigation.new_move_incm(tank, 32, 30)
    tank.on_for_rotations(0, 30, 0.8)
    tank.on_for_rotations(0, -30, 0.8)
    Navigation.gyro_check(tank, 5, 0)


    #Go forward more
    Navigation.new_move_incm(tank, 34, 28)


    #Turn and Go to SwitchE
    tank.turn_degrees(10, 40, True, 1)
    Navigation.gyro_check(tank, 5, 40)

    Navigation.new_move_incm(tank, 30, 15)
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
    #Navigation.gyro_check(tank, 5, 7)


    lift.reset()
    lift.on_for_rotations(60, 8)
    lift.reset()
    lift.on_for_rotations(-60, 0.6)
    lift.reset()

    lift.on_for_rotations(60, 8)
    lift.reset()
    lift.on_for_rotations(60, -8)

    #Do green cargo mission
    #OG val 3, then 2
    Navigation.distance_to_object(tank, 1.4, "Forward")

    #Og val=.35
    tank.on_for_rotations(10, 0, .225)

    #Go forward and grab grey cargo
    Navigation.distance_to_object(tank, 10, "Forward")
    lift.on_for_rotations(60, 8)

    #Go back to put grey cargo in grey circle

    Navigation.distance_to_object(tank, 10, "Backward")
    #Navigation.new_move_incm(tank, -25, 10)
    lift.on_for_rotations(60, -8)
    #Navigation.distance_to_object(tank, 10, "Backward")

    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))

    return
    Navigation.new_move_incm(tank, -100, 40)
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
    #PraticeCode()
