#!/usr/bin/env python3
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
import NorthWestSide
import truck
import Navigation

btn = Button()

    #PUT THE FUNCTION IN THE ELSE STATEMENT
def left(state):
    if state:
        pass
    else:
        truck.truck_3(Navigation.tank_init())

def right(state):
    if state:
        pass
    else:
        pass

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



def run():
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





#Execute Northide Missions
if __name__ == "__main__":
    run()
