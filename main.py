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
    #Latest version of executing the latest functions (yeah I know, it's repetitive)
    def left(state):
        if state:
            pass
        else:
            NorthWestSide.Coach_Code(tank,lift,Claw)
            tank.gyro.reset()
            lift.reset()
    def right(state):
        if state:
            pass
        else:
            truck.truck_4(tank, lift, Claw)

    def up(state):
        if state:
            pass
        else:
            Sorter.NewerIdea(tank, lift, Claw, 1)
    def down(state):
        if state:
            pass
        else:
            Sorter.NewerIdea(tank, lift, Claw, 3)


    def enter(state):
        if state:
            pass
        else:
            Sorter.NewerIdea(tank, lift, Claw, 2)

    # Menu items
    #list = init.main_menu

    # Load the main menu on the console
    #message.display_menu(list)
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
    while True:
        btn.process()
        sleep(0.01)

if __name__ == "__main__":
    main()
