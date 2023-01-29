#!/usr/bin/env python3

import ev3dev.ev3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
import time, init
import os
import Run1
import tvrun
import Navigation
import PodSA
import tvrun


# Main program
def main():
    #Set Up
    sound = Sound()
    tank = Navigation.tank_init()
    btn = Button()#hi
    flipper = LargeMotor(OUTPUT_C)
    colorful_flipper = flipper
    flip_flop = MediumMotor(OUTPUT_D)

    #Reset
    tank.reset()
    tank.gyro.reset()
    flipper.reset()
    flip_flop.reset()

    os.system('setfont Lat15-TerminusBold32x16')
    sound.play_tone(1500,0.3) #gyro is working!


    #PUT THE FUNCTION IN THE ELSE STATEMENT
    #Latest version of executing the latest functions (yeah I know, it's repetitive)
    def left(state):
        if state:
            pass
        else:
            try:
                print("Platform")
                tank.gyro.reset()
                starttime = time.time()
                Run1.PlatformRun(tank, flipper, flip_flop)
                init.debug_print(time.time()-starttime)
                print(time.time()-starttime)
                tank.reset()
                flipper.reset()
                flip_flop.reset()
            except (RuntimeError, TypeError, NameError, SyntaxError):
                tank.reset()
                tank.gyro.reset()
                flipper.reset()
                flip_flop.reset()
                pass

    def up(state):
        if state:
            pass
        else:
            try:
                starttime = time.time()
                print("Dino Run")
                tank.gyro.reset()
                PodSA.newest_dino_powerplant(tank, flipper, flip_flop)
                init.debug_print(time.time()-starttime)
                tank.reset()
                flipper.reset()
                flip_flop.reset()
            except (RuntimeError, TypeError, NameError, SyntaxError):
                tank.reset()
                tank.gyro.reset()
                flipper.reset()
                flip_flop.reset()
                pass

    def right(state):
        if state:
            pass
        else:
            try:
                print("TV Run")
                tank.gyro.reset()
                tvrun.tv(tank, colorful_flipper)
                tvrun.windmill(tank, colorful_flipper)
                tvrun.toystory3(tank, colorful_flipper)
                tank.reset()
                flipper.reset()
                flip_flop.reset()

            except (RuntimeError, TypeError, NameError, SyntaxError):
                tank.reset()
                tank.gyro.reset()
                flipper.reset()
                flip_flop.reset()
                pass

    def down(state):
        if state:
            pass
        else:
            try:
                print("Innov Run")
                tank.gyro.reset()
                PodSA.finalwater_reservoir_hangonhook(tank, flipper, flip_flop)
                tank.reset()
                flipper.reset()
                flip_flop.reset()
            except (RuntimeError, TypeError, NameError, SyntaxError):
                tank.reset()
                tank.gyro.reset()
                flipper.reset()
                flip_flop.reset()
                pass

    def enter(state):
        if state:
            pass

        else:
            try:
                print("Energy Storage")
                tank.gyro.reset()
                starttime = time.time()
                Run1.EnergyStorage(tank, flipper, flip_flop)
                init.debug_print(time.time()-starttime)
                print(time.time()-starttime)
                tank.reset()
                flipper.reset()
                flip_flop.reset()
            except (RuntimeError, TypeError, NameError, SyntaxError):
                tank.reset()
                tank.gyro.reset()
                flipper.reset()
                flip_flop.reset()
                pass

    btn.on_left = left
    btn.on_right = right
    btn.on_up = up
    btn.on_down = down
    btn.on_enter = enter

    # This loop checks button states continuously (every 0.01s).
    # If the new state differs from the old state then the appropriate
    # button event handlers are called.
    '''
            tank.gyro.reset()
            tank.turn_degrees(10,90)
            print(tank.gyro.angle)
            sleep(2)
            tank.turn_degrees(10,90)
            print(tank.gyro.angle)
            sleep(2)
            tank.turn_degrees(10,90)
            print(tank.gyro.angle)
            sleep(2)
            tank.turn_degrees(10,90)
            print(tank.gyro.angle)
            sleep(2)
            '''
    sound.play_tone(2500,0.1)
    sound.play_tone(2000,0.1) #everythig is working fine now
    while True:
        print(tank.gyro.angle)
        btn.process()
        sleep(0.01)

if __name__ == "__main__":
    main()
