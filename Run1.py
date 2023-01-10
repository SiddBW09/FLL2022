#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep, time
import Navigation, init
from threading import Thread
from ev3dev2.sound import Sound


# def timer(startTime, timelimit):
#     while True:
#         if time() - startTime >= timelimit:
#             sound = Sound()
#             sound.play_tone(2500,0.1)
#             sound.play_tone(2000,0.1) #everythig is working fine now
#             break



def PlatformRun(tank, flipper):
    flip_flop = MediumMotor(OUTPUT_D)
    tank.gyro.reset()
    flipper.reset()

    AnotherWateryThingy(tank, flipper)

    #WateryThingy(tank, flipper)
    FlameThingy(tank, flipper)

    Boxythingy(tank, flipper)

    NewyCody(tank, flipper)


    HighFiveyThingy(tank, flipper)

    CaryThingy(tank, flipper)

def PlatformRunUpdate(tank, flipper):
    tank.gyro.reset()
    flipper.reset()

    OilandHydro(tank, flipper)

    Sweeper(tank, flipper)

    GrabNGo(tank, flipper)
    return

    HighFiveyThingy(tank, flipper)

    CaryThingy(tank, flipper)

def OilandHydro(tank, flipper):
    flip_flop = MediumMotor(OUTPUT_D)
    #Flip filipper down, and go to Oil platform
    flipper.on_for_rotations(30, 0.45)
    Navigation.distance_goer(tank, 54, -30, 0)

    #Do oil platform and hydro dam at once
    flip_flop.on_for_rotations(20, 0.2)

    for x in range(3):
        flipper.on_for_rotations(-15, 0.12)
        flip_flop.on_for_rotations(-15, 0.2)
        flipper.on_for_rotations(15, 0.12)
        flip_flop.on_for_rotations(15, 0.2)

    flip_flop.on_for_rotations(-20, 0.1)

    #Turn and go to sweeper
    Navigation.gyro_check(tank, 5, 45)

    Navigation.distance_goer(tank, 38, -20, 45)
    Navigation.gyro_check(tank, 5, 90)
    Navigation.gyro_check(tank, 5, 90)



def AnotherWateryThingy(tank, flipper):
    flipper.on_for_rotations(30, 0.3)
    Navigation.distance_goer(tank, 44, -30, 0)

    # Turn to Hydro Dam
    Navigation.gyro_check(tank, 5, 50)
    flipper.on_for_rotations(-30, 0.2)
    Navigation.gyro_check(tank, 5, 0)
    flipper.on_for_rotations(30, 0.35)

'''def WateryThingyOld(tank, flipper):
    tank.gyro.reset()
    flipper.on_for_rotations(30, 0.3)
    Navigation.distance_goer(tank, 33, -25, 0)
    Navigation.gyro_check(tank, 5, 5)
    flipper.on_for_rotations(-30, 0.3)
    Navigation.goer_no_gyro(tank, 6, 20)
    sleep(0.1)
    Navigation.gyro_check(tank, 4, -4)
    sleep(0.1)
    Navigation.gyro_check(tank, 4, -44)
    flipper.on_for_rotations(30, 0.45)'''

'''def WateryThingy(tank, flipper):
    tank.gyro.reset()
    flipper.on_for_rotations(30, 0.3)
    Navigation.distance_goer(tank, 35, -25, 0)
    Navigation.gyro_check(tank, 5, 5)
    flipper.on_for_rotations(-30, 0.3)
    Navigation.goer_no_gyro(tank, 8, 20)
    sleep(0.1)
    Navigation.gyro_check(tank, 4, -4)
    sleep(0.1)
    Navigation.gyro_check(tank, 4, -45)
    flipper.on_for_rotations(30, 0.1)
    '''

def FlameThingy(tank, flipper):
    #Go to Oil
    Navigation.distance_goer(tank, 9.5, -20, 0)

    #Do the mission
    for x in range(2):
        flipper.on_for_rotations(-15, 0.12)
        flipper.on_for_rotations(15, 0.12)
    flipper.on_for_rotations(-20, 0.12)

    #Go back
    Navigation.distance_goer(tank, 4.5, 15, 0)

    #Turn and go forward
    Navigation.gyro_check(tank, 10, 22)
    Navigation.distance_goer(tank, 14, -15,22)

    #Straight for Boxy
    Navigation.gyro_check(tank, 5, 0)


def Boxythingy(tank, flipper):
    #Forward to Boxy
    Navigation.distance_goer(tank, 12, -15, 0)

    #Grab tray, pull back it back, and flip it
    flipper.on_for_rotations(30, 0.12)
    Navigation.distance_goer(tank, 7, 10, 0)
    sleep(0.2)
    flipper.on_for_rotations(-80, 0.45)

    #Turn and go to sweep place
    Navigation.gyro_check(tank, 10, 45)
    Navigation.distance_goer(tank, 17, -10, 45)
    Navigation.gyro_check(tank, 10, 90)
    init.debug_print("After boxy: ", tank.gyro.angle)


''''def MoveyThingy(tank, flipper):
    tank.gyro.reset()
    Navigation.gyro_check(tank, 10, 35)
    flipper.on_for_rotations(10, 0.4)
    Navigation.distance_goer(tank, 19, -25, 35)
    flipper.on_for_rotations(-10, 0.14)
    Navigation.gyro_check(tank, 5, 70)
    flipper.on_for_rotations(10, 0.14)
    Navigation.distance_goer(tank, 19, -30, 70)
    Navigation.gyro_check(tank, 5, 90)'''

def NewyCody(tank, flipper):
    flip_flop = MediumMotor(OUTPUT_D)

    #Go and sweep units
    Navigation.gyro_check(tank, 5, 90)
    flip_flop.on_for_rotations(20, -0.35)
    Navigation.distance_goer(tank, 36, -30, 90)

    #Flipper up
    flip_flop.on_for_rotations(7, 0.35)

    #Turn and head towards highfive
    Navigation.gyro_check(tank, 5, 135)
    Navigation.distance_goer(tank, 23, -20, 135)

    #Turn so facing highfive
    Navigation.gyro_check(tank, 10, 0)

def Sweeper(tank, flipper):
    flip_flop = MediumMotor(OUTPUT_D)

    Navigation.gyro_check(tank, 5, 90)
    Navigation.distance_goer(tank, 8, 5, 90)
    Navigation.gyro_check(tank, 5, 90)

    flipper.on_for_rotations(-15, 0.35)

    #Lower flip to sweep
    flip_flop.on_for_rotations(-15, 0.5)

    #SWEEEEEP is here OG speed -20
    Navigation.distance_goer(tank, 29, -30, 90)
    return

def GrabNGo(tank, flipper):
    flip_flop = MediumMotor(OUTPUT_D)

    #Raise Flip
    flip_flop.on_for_rotations(20, 0.35)


    Navigation.gyro_check(tank, 5, 180)
    flip_flop.on_for_rotations(10, -0.1)
    Navigation.gyro_check(tank, 5, 180)
    # flip_flop.on_for_rotations(-20, 0.15)
    Navigation.distance_goer(tank, 26, 15, 180)

    flipper.on_for_rotations(20, 0.375) #og VAL 0.35
    #flipper.reset()

    Navigation.gyro_check(tank, 5, 180)

    #Grab Hydro Units, Turn, and go to Left Home
    Navigation.distance_goer(tank, 19, -15, 185)
    Navigation.gyro_check(tank, 5, 165)
    Navigation.distance_goer(tank, 52, -20, 165)
    Navigation.gyro_check(tank, 5, 255)
    Navigation.goer_no_gyro(tank, 70, -60)


def HighFiveyThingy(tank, flipper):
    flipper.on_for_rotations(20, 0.3)

    #Go towards highfive
    Navigation.distance_goer(tank, 7.5, -10, 0)

    #Pull back highfive
    flipper.on_for_rotations(10, 0.15)
    sleep(0.2)
    Navigation.distance_goer(tank, 7, 15, 0)
    sleep(0.2)
    flipper.on_for_rotations(-20, 0.4)

    #Go and turn for car
    Navigation.goer_no_gyro(tank, 4, -10)
    Navigation.gyro_check(tank, 5, -90)

def CaryThingy(tank, flipper):

    #Go forward and turn to car
    Navigation.distance_goer(tank, 36, 20 , -90)
    Navigation.gyro_check(tank, 5, -50)
    flipper.on_for_rotations(15, 0.45)
    Navigation.distance_goer(tank, 4, -5, -50)

    #Turn parallel to car
    Navigation.gyro_check(tank, 5, -40)

    #Roll the car out, and lower the bar
    flipper.on_for_rotations(-5, 0.45)
    flipper.on_for_rotations(20, 0.45)

    #Go to left home
    Navigation.distance_goer(tank, 85, 40, -42)
    flipper.on_for_rotations(-30, 0.45)

def DinoRun(tank, flipper):
    flip_flop = MediumMotor(OUTPUT_D)
    flip_flop.reset()
    flip_flop.on_for_degrees(30, 10)
    #Go to right home
    flipper.on_for_rotations(-10, 0.05)
    tank.gyro.reset()
    Navigation.distance_goer(tank, 86, -35, 0)
    sleep(0.1)
    flip_flop.on_for_degrees(50, 80)
    Navigation.distance_goer(tank, 82, -60, 0)

def new_dino_run_for_power_plant(tank, flipper):
    flip_flop = MediumMotor(OUTPUT_D)
    flip_flop.reset()

    #Navigation.goer_no_gyro(tank, 30, -25)

    #operate mission
    Navigation.distance_goer(tank, 82, -40, 0)
    init.debug_print("After boxy: ", tank.gyro.angle)
    flip_flop.on_for_degrees(40, 90)
    Navigation.distance_goer(tank, 17, 25, 0)
    #Navigation.gyro_check(tank, 10, -4)

    #Flip thingy up
    flipper.on_for_rotations(10, 0.5)

    sleep(0.2)
    Navigation.gyro_check(tank, 10, 0)
    #go to home
    Navigation.distance_goer(tank, 35, -35, 0)
    Navigation.gyro_check(tank, 10, 18)
    Navigation.distance_goer(tank, 15, -25, 18)
    Navigation.gyro_check(tank, 10, 0)
    Navigation.goer_no_gyro(tank, 60, -50)

def newnew_dino_powerplant(tank, flipper):
    flip_flop = MediumMotor(OUTPUT_D)
    flip_flop.reset()

    #Navigation.goer_no_gyro(tank, 30, -25)

    #operate mission
    Navigation.distance_goer(tank, 82, -40, 0)
    init.debug_print("After boxy: ", tank.gyro.angle)

    #Flip this up
    flip_flop.on_for_degrees(40, 90)

    #Go back from power plant and turn left and go forward in line for the Great Flick
    Navigation.distance_goer(tank, 30, 25, 0)
    #mstuff

    #Turn away from power plant and go at angle -35
    Navigation.gyro_check(tank, 10, -35)
    Navigation.distance_goer(tank, 13, -25, -35)

    #Go back to be parallel
    Navigation.gyro_check(tank, 10, 0)
    Navigation.distance_goer(tank, 3, -10, 0)

    #Flip this down energy unit
    flipper.on_for_rotations(20, 0.5)

    #Go away from power plant because sahana is a bozo
    Navigation.distance_goer(tank, 10, 25, 0)

    #Turn at  angle 30 and go, then turn back to 0 so Evie is parallel to Power Plant
    Navigation.gyro_check(tank, 10, 30)
    Navigation.distance_goer(tank, 20, -25, 30)
    Navigation.gyro_check(tank, 10, 0)

    #Go forward and turn to hydro dam and sweep it away
    Navigation.distance_goer(tank, 46, -25, 0)

        #lift flippy up, turn, and put it down to catch hydro dam nrg unit
    flipper.on_for_rotations(20, -0.5)
    Navigation.gyro_check(tank, 10, 14)
    flipper.on_for_rotations(20, 0.5)
    return

    Navigation.distance_goer(tank, 60, -60, 13.5)
    #Navigation.distance_goer(tank, 5, -25, 0)

    #Navigation.gyro_check(tank, 10, -4)

    #Flip down down
    #flipper.on_for_rotations(10, 0.5)
    return

    sleep(0.2)
    Navigation.gyro_check(tank, 10, 0)
    #go to home
    Navigation.distance_goer(tank, 35, -35, 0)
    Navigation.gyro_check(tank, 10, 18)
    Navigation.distance_goer(tank, 15, -25, 18)
    Navigation.gyro_check(tank, 10, 0)
    Navigation.goer_no_gyro(tank, 60, -50)

def Dump_3(tank, flipper):
    #Move forward
    Navigation.distance_goer(tank, 5, -20, 0)
    Navigation.gyro_check(tank, 5, 0)

    #Turn and go forward
    Navigation.gyro_check(tank, 5, 22)
    Navigation.distance_goer(tank, 10, -20, 22)
    Navigation.gyro_check(tank, 5, 22)

    #Straight for Boxy
    Navigation.gyro_check(tank, 10, 0)

    #Go to boxy thingy
    Navigation.distance_goer(tank, 63, -25, 0)
    Navigation.gyro_check(tank, 10, 0)
    flipper.on_for_rotations(20, 0.15)

    #Move back
    Navigation.distance_goer(tank, 27, 20, 0)

    #Lower flip
    flipper.on_for_rotations(15, 0.24)

    Navigation.gyro_check(tank, 10, 54)
    Navigation.distance_goer(tank, 38, 25, 54)
    Navigation.gyro_check(tank, 10, 0)
    Navigation.distance_goer(tank,6, -15, 0,)
    Navigation.gyro_check(tank, 10, -10)
    tank.on_for_rotations(30, 35, 2)
    #  Navigation.distance_goer(tank, 30, 40, -22)

    return
    Navigation.gyro_check(tank, 20, -115)
    Navigation.distance_goer(tank, 15, -20, -115)
    return

    #flipper.on_for_rotations(-10, 0.1)
    Navigation.gyro_check(tank, 10, 180)

    return
    Navigation.distance_goer(tank, 40, 20, 0)
    Navigation.gyro_check(tank, 5, 0)

    return
    #Turn
    Navigation.gyro_check(tank, 5, 60)

    #Move back
    Navigation.distance_goer(tank, 11, 20, 45)

    #Move Oil Platform
    Navigation.gyro_check(tank, 10, -130)

if __name__ == "__main__":
    tank = Navigation.tank_init()
    flipper = LargeMotor(OUTPUT_C)
    time1 = time()
    # timeThread = Thread(target=timer, args=(time(), 5,))
    # timeThread.start()
    #DinoRun(tank, flipper)
    #new_dino_run_for_power_plant(tank, flipper)
    #newnew_dino_powerplant(tank, flipper)
    #PlatformRunUpdate(tank, flipper)
    Dump_3(tank, flipper)
    init.debug_print(time()-time1)
