#!/usr/bin/env python3

import ev3dev.ev3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
import os
import Run1
import tvrun
import Navigation
import PodSA
import tvrun


# Main program
def main():
    sound = Sound()
    tank = Navigation.tank_init()
    tank.gyro.reset()
    sound.play_tone(1500,0.3) #gyro is working!
    btn = Button()#hi
    flipper = LargeMotor(OUTPUT_C)
    os.system('setfont Lat15-TerminusBold32x16')

    #PUT THE FUNCTION IN THE ELSE STATEMENT
    #Latest version of executing the latest functions (yeah I know, it's repetitive)
    def left(state):
        if state:
            pass
        else:
            tvrun.tv()
            tvrun.windmill()
            tvrun.toystory3()
            flipper.reset()



    def right(state):
        if state:
            pass
        else:
            Run1.DinoRun(tank, flipper)
            flipper.reset()
            pass

    def up(state):
        if state:
            pass
        else:
            try:
                Run1.PlatformRun(tank, flipper)
                flipper.reset()
            except (RuntimeError, TypeError, NameError, SyntaxError):
                tank.reset()
                tank.gyro.reset()
                flipper.reset()
                pass

    def down(state):
        if state:
            pass
        else:
            PodSA.InnovMission(tank,flipper)
            flipper.reset()
            pass

    def enter(state):
        if state:
            pass
        else:
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
