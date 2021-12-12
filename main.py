#!/usr/bin/env python3

import ev3dev.ev3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import init
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
import claw
import NorthWestSide
import truck
import Navigation
import Sorter


# Main program
def main():

    tank = Navigation.tank_init()
    lift = MediumMotor(OUTPUT_D)
    #import claw
    Claw = claw.Claw()
    btn = Button()

    #PUT THE FUNCTION IN THE ELSE STATEMENT
    def left(state):
        if state:
            pass
        else:
            truck.truck_3(tank,Claw)

    def right(state):
        if state:
            pass
        else:
            Sorter.completeRun(tank, lift, Claw)

    def up(state):
        if state:
            pass
        else:
            NorthWestSide.Coachie_Code()

    def down(state):
        if state:
            pass
        else:
            pass

    def enter(state):
        if state:
            pass
        else:
            pass


    # Menu items
    #list = init.main_menu

    # Load the main menu on the console
    #message.display_menu(list)
    init.debug_print("main nothing to do")

if __name__ == "__main__":
    main()
