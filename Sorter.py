#!/usr/bin/env python3

import ev3dev.ev3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from time import sleep
from ev3dev2.sound import Sound
import init
import claw
import Navigation





def BlueInTheCenterRun(tank, Lift, claw):
    x = 0
    init.debug_print("In current run")
    my_tank = tank
    lift = Lift
    MyClaw = claw
    MyClaw.claw.reset()
    lift.reset()
    my_tank.reset()
    my_tank.gyro.reset()
    #start of code
    #Putting the train track down
    lift.on_for_rotations(30, -1.4)
    lift.reset()
    my_tank.on_for_rotations(10, 10, 0.7)
    lift.on_for_rotations(10, 0.6)
    my_tank.on_for_rotations(15, 15, -0.7)
    sleep(0.5)
    MyClaw.claw_open(100)
    my_tank.turn_degrees(10, 90, True, 1)
    Navigation.gyro_check(my_tank, 10, 90)
    init.debug_print("Turned degrees to pick up brick" + str(my_tank.gyro.angle))
    my_tank.on_for_rotations(10, 10, -0.1)
    #Goes down to pick up blue container
    lift.on_for_rotations(49, 0.7)
    MyClaw.claw.reset()
    if MyClaw.claw_close(100):
        init.debug_print("Found blue brick")
        sleep(0.5)
        lift.on_for_rotations(49, -3)
        my_tank.turn_degrees(10, -90, True, 1)
        Navigation.gyro_check(my_tank, 10, -90)
        Navigation.distance_to_object(my_tank, 43, "Forward", 10 )
        lift.on_for_rotations(49, 3)
        sleep(1)
        #Drops blue block
        MyClaw.claw_open(100)
        sleep(0.5)
        lift.on_for_rotations(35, -0.8)
        #Turn to hit the helicopter
        my_tank.turn_degrees(10, -90, True, 1)
        #Navigation.gyro_check(my_tank, 10, -95)
        init.debug_print("Turned degrees" + str(my_tank.gyro.angle))
        #Navigation.gyro_check(my_tank, 10, -120)

        my_tank.on_for_rotations(15, 15, -0.5)

        my_tank.on_for_rotations(15, 15, 0.32)
        #target angle is -275
        my_tank.turn_degrees(10, -120, True, 1)
        my_tank.on_for_rotations(15, 15, 0.5)
        turn_angle = -1* (270 + (my_tank.gyro.angle))
        init.debug_print("Turned degrees" + str(turn_angle))
        my_tank.turn_degrees(10, turn_angle, True, 1)
        #Last left of

        init.debug_print("Turned degrees" + str(my_tank.gyro.angle))
        my_tank.gyro.reset()
        lift.on_for_rotations(30, 0.4)
        Navigation.distance_to_object(my_tank, 43, "Forward", 10)
        return

def GreenInFirstSlot(tank, lift, claw):
        #init.debug_print("nothing for now")
        Navigation.distance_to_object(my_tank, 1, "Backwards", 10)
        lift.on_for_rotations(30, -0.2)




def SlotToCircle(x):
    #move to
    my_tank.on_for_rotations(15, 15, -0.3)
    my_tank.on_for_rotations(15, 0, 0.85)
    my_tank.on_for_rotations(25, 25, x)
    lift.on_for_rotations(49, 3)
    sleep(0.5)
    claw.claw_open(100)

def CircleToSlot():
    my_tank.on_for_rotations(15, 15, -0.75)
    my_tank.on_for_rotations(-15, 15, 0.5)
    my_tank.on_for_rotations(15, 15, 0.2)


def no_detection():
    claw.claw_open(100)
    lift.on_for_rotations(49, -3)
    my_tank.on_for_rotations(15, 15, 0.3)
    claw.claw_open(100)
    lift.on_for_rotations(49, 3)
    claw.claw_close(100)
    lift.on_for_rotations(49, -3)


def Have_brick(lift):

    init.debug_print("Have brick")
    i = 0
    lift.reset()
    while True:
        init.debug_print("In loop")
        lift.on_for_rotations(5, 0.1, brake=False)
        init.debug_print(lift.state)
        if 'stalled' in lift.state:
            init.debug_print(lift.state)
            break
        i += 1
    init.debug_print(i)
    if (i > 15):
     return False
    return True

def second_check():
    my_tank.on_for_rotations(15, 15, 0.4)
    MyClaw.claw_open(100)
    lift.on_for_rotations(49, 3)
    MyClaw.claw_close(100)
    lift.on_for_rotations(49, -3)


#
'''claw.claw_open(100)
lift.on_for_rotations(49, 2.5)
if claw.claw_close(100):
    lift.on_for_rotations(49, -3)
    SlotToCircle(0.85)
    lift.on_for_rotations(49, 3)
    sleep(1)
    claw.claw_open(100)
    sleep(0.5)
    lift.on_for_rotations(49, -3)
    CircleToSlot()
else:
    no_detection()
    my_tank.on_for_rotations(15, 15, -0.3)
    SlotToCircle(0.85)'''


'''my_tank.on_for_rotations(15, 15, 0.15)
claw.claw_open(100)
sleep(0.5)
lift.on_for_rotations(49, 3)
sleep(0.5)
claw.claw_close(100)
sleep(0.5)
lift.on_for_rotations(49, -3)'''

if __name__ == "__main__":
    #train()
    BlueInTheCenterRun(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #GreenInFirstSlot(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())

    #train(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
