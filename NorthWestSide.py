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



    #Lift up at start
    Sorter.motor_check(60, 3, lift)




    #Go to blue mission thing
    Navigation.distance_goer(tank, 30, 32, 0)
    tank.on_for_rotations(0, 30, 0.8)
    tank.on_for_rotations(0, -30, 0.8)
    Navigation.gyro_check(tank, 5, 0)




    #Go forward more

    Navigation.distance_goer(tank, 28, 40, 0)




    #Turn and Go to SwitchE
    tank.turn_degrees(10, 40, True, 1)
    Navigation.gyro_check(tank, 5, 40)




    Navigation.distance_goer(tank, 15, 30, 40)

    Navigation.gyro_check(tank, 5, 40)
    Navigation.distance_goer(tank, 12, 20, 40)



    Navigation.distance_goer(tank, 6.5, 10, 40)
    Navigation.gyro_check(tank, 10, 50)



    lift.on_for_rotations(-70, 5)





    #Go back to home
    #OG val=- -30, 37
    Navigation.gyro_check(tank, 10, 60)
    Navigation.distance_goer(tank, 41, -40, 60)
    Navigation.gyro_check(tank, 10, 25)


    lift.reset()
    lift.on_for_rotations(60, 8)
    lift.reset()
    lift.on_for_rotations(-60, 0.6)
    lift.reset()



    lift.on_for_rotations(60, 8)
    lift.reset()
    lift.on_for_rotations(60, -8)



    #Do gray cargo mission
    Navigation.gyro_check(tank, 10, 45)



    #Go forward and grab grey cargo
    Navigation.distance_goer(tank, 15, 20, 45)
    sleep(1)
    Sorter.motor_check(60, 8, lift)



    #Go back to put grey cargo in grey circle
    Navigation.distance_goer(tank, 9, -20, 45)
    lift.on_for_rotations(60, -8)
    sleep(0.5)



    '''endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))'''



    #return
    Navigation.distance_goer(tank, 40, -25, 40)
    tank.turn_degrees(10, -30, True, 1)



    #init.debug_print(int(time.time()-start_time))
    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))
    lift.reset()
    Claw.claw.reset()







#Execute Northide Missions
if __name__ == "__main__":
    Coach_Code(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())

