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

    #Go to right home
    flipper.on_for_rotations(-10, 0.05)
    tank.gyro.reset()
    Navigation.distance_goer(tank, 163, -60, 0)

if __name__ == "__main__":
    tank = Navigation.tank_init()
    flipper = LargeMotor(OUTPUT_C)
    time1 = time()
    # timeThread = Thread(target=timer, args=(time(), 5,))
    # timeThread.start()
    PlatformRun(tank, flipper)
    init.debug_print(time()-time1)
