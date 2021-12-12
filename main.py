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
            NorthWestSide.Coachie_Code(tank,lift,Claw)

    def down(state):
        if state:
            pass
        else:
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

    def enter(state):
        if state:
            pass
        else:
            for i in range(3):
                tank.on_for_rotations(15, 15, 1)
                tank.on_for_rotations(15, 15, -1)
            for i in range(3):
                lift.on_for_rotations(-20,4)
                lift.on_for_rotations(20,4)
            for i in range(3):
                Claw.claw_close(100)
                Claw.claw_open(100)
            tank.reset()
            lift.reset()
            Claw.claw.reset()

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
    while True:
        btn.process()
        sleep(0.01)

if __name__ == "__main__":
    main()
