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
import Sorter



def Coach_Code(tank, lift, Claw):
    #tank = Navigation.tank_init()
    #lift = MediumMotor(OUTPUT_D)
    #Claw = claw.Claw()
    tank.gyro.reset()
    start_time = time.time()



    #Lift down at start
    Sorter.motor_check(60, 3, lift)
    lift.reset()




    #Go to blue mission thing
    Navigation.distance_goer(tank, 30, 35, 0)
    tank.on_for_rotations(0, 40, 0.8)
    tank.on_for_rotations(0, -40, 0.8)
    Navigation.gyro_check(tank, 8, 0)




    #Go forward more
    Navigation.distance_goer(tank, 30, 35, 0)




    #Turn and Go to SwitchE
    Navigation.gyro_check(tank, 5, 40)

    Navigation.distance_goer(tank, 28, 35, 40)
    sleep(0.1)
    Navigation.gyro_check(tank, 5, 50)
    lift.on_for_rotations(-70, 5)
    sleep(0.1)


    #Go back to home
    Navigation.gyro_check(tank, 5, 60)
    Navigation.distance_goer(tank, 39, -35, 60)
    sleep(0.4)
    Navigation.gyro_check(tank, 5, 25)
    #init.debug_print(tank.gyro.angle)



    lift.reset()
    Sorter.motor_check(80, 8, lift)
    lift.reset()
    Sorter.motor_check(-80, 8, lift)
    lift.reset()




    #Do gray cargo mission
    Navigation.gyro_check(tank, 8, 45)



    #Go forward and grab grey cargo
    Navigation.distance_goer(tank, 18, 35, 45)
    sleep(0.2)
    Sorter.motor_check(60, 8, lift)
    sleep(0.2)



    #Go back to put grey cargo in grey circle
    Navigation.distance_goer(tank, 10, -15, 45)
    lift.on_for_rotations(-60, 8)
    sleep(0.5)



    '''endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))'''



    #return
    # Navigation.distance_goer(tank, 40, -40, 40)
    tank.on_for_rotations(-50, -50, 1.2)
    tank.on_for_rotations(0, 30, 0.3)



    #init.debug_print(int(time.time()-start_time))
    endtime = time.time()-start_time
    #init.debug_print("TIME: "+str(endtime))
    lift.reset()
    Claw.claw.reset()

    #Testing:
    #1 S
    #2 CP didn't work
    #3 S
    #4
    #5
    #6



#Execute Northide Missions
if __name__ == "__main__":
    Coach_Code(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())

