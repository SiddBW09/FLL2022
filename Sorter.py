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


def current_run(tank, Lift, claw):
    x = 0
    init.debug_print("In current run")
    my_tank = tank
    lift = Lift
    MyClaw = claw
    MyClaw.claw.reset()
    lift.reset()
    my_tank.reset()
    #start of code
    lift.on_for_rotations(30, -1.5)
    my_tank.on_for_rotations(10, 10, 0.7)
    sleep(0.5)
    lift.on_for_rotations(10, 0.6)
    my_tank.on_for_rotations(15, 15, -0.7)
    sleep(0.5)
    lift.on_for_rotations(10, -0.3)
    MyClaw.claw_open(150)
    my_tank.turn_degrees(10, 90, True, 1)
    init.debug_print("Turned degrees to pick up brick" + str(my_tank.gyro.angle))
    my_tank.on_for_rotations(15, 15, -0.07 )
    #Goes down to pick up blue container
    lift.on_for_rotations(10, 1)
    MyClaw.claw.reset()
    if MyClaw.claw_close(100):
        init.debug_print("Found blue brick")
        sleep(1)
        lift.on_for_rotations(49, -3)
        my_tank.turn_degrees(10, -180, True, 1)

        Navigation.gyro_check(my_tank, 10, -90)
        init.debug_print("Turned degrees to turn to drop blue" + str(my_tank.gyro.angle))
        Navigation.distance_to_object(my_tank, 43, "Forward", 10 )
        lift.on_for_rotations(49, 3)
        sleep(1)
        MyClaw.claw_open(100)
        sleep(0.5)
        lift.on_for_rotations(35, -0.8)
        #Turn to hit the helicopter
        my_tank.turn_degrees(10, -90, True, 1)
        init.debug_print("Turn to chopper" + str(my_tank.gyro.angle))
        #Navigation.gyro_check(my_tank, 10, -120)

        my_tank.on_for_rotations(15, 15, -0.195)


        my_tank.on_for_rotations(15, 15, 0.35)
        #target angle is -275

        my_tank.turn_degrees(10, -90, True, 1)
        return
        my_tank.on_for_rotations(15, 15, 0.5)

        turn_angle = -1* (270 + (my_tank.gyro.angle))
        init.debug_print("Turned degrees" + str(turn_angle))
        my_tank.turn_degrees(10, turn_angle, True, 1)


def blue_two_slot_one(tank, Lift, claw):
    x = 0
    init.debug_print("In current run")
    my_tank = tank
    lift = Lift
    MyClaw = claw
    MyClaw.claw.reset()
    lift.reset()
    my_tank.reset()
    #start of code
    lift.on_for_rotations(30, -1.5)
    my_tank.on_for_rotations(10, 10, 0.7)
    sleep(0.5)
    lift.on_for_rotations(10, 0.6)
    my_tank.on_for_rotations(15, 15, -0.7)
    sleep(0.5)
    lift.on_for_rotations(10, -0.3)
    MyClaw.claw_open(150)
    my_tank.turn_degrees(10, 90, True, 1)
    init.debug_print("Turned degrees to pick up brick" + str(my_tank.gyro.angle))
    my_tank.on_for_rotations(15, 15, -0.07 )
    #Goes down to pick up blue container
    lift.on_for_rotations(10, 1)
    MyClaw.claw.reset()
    if MyClaw.claw_close(100):
        init.debug_print("Found blue brick")
        sleep(1)
        lift.on_for_rotations(49, -3)

        Navigation.gyro_check(my_tank, 10, 90)
        init.debug_print("Turned degrees to turn to drop blue" + str(my_tank.gyro.angle))
        Navigation.distance_to_object(my_tank, 36, "Backward", 10)

        #Turn to Helicopter
        tank.turn_degrees(10, 50, True, 1)
        Navigation.gyro_check(my_tank, 10, 140)
        init.debug_print("Chopper turn" + str(my_tank.gyro.angle))
        Navigation.distance_to_object(tank, 8, "Backward")
        Navigation.distance_to_object(tank, 9, "Forward")
        init.debug_print("Chopper turn_two" + str(my_tank.gyro.angle))



        #Turn to Blue Circle
        tank.turn_degrees(10, 132, True, 1)
        Navigation.gyro_check(my_tank, 10, 270)
        init.debug_print("Dropping blue turn" + str(my_tank.gyro.angle))
        Navigation.distance_to_object(tank, 3, "Forward")
        sleep(0.5)
        lift.reset()
        lift.on_for_rotations(49, 1.7)
        sleep(0.5)
        MyClaw.claw_open(100)
        sleep(0.5)
        lift.on_for_rotations(49, -1.7)
        Navigation.distance_to_object(tank, 15, "Backward")
        Navigation.gyro_check(tank, 10, 270)
        tank.gyro.reset()
        return
        tank.turn_degrees(10, -180, True, 1)
        Navigation.gyro_check(tank, 10, 90)
        init.debug_print("Alligning turn" + str(my_tank.gyro.angle))
        tank.gyro.reset()

        return


        lift.on_for_rotations(49, 3)
        sleep(1)
        MyClaw.claw_open(100)
        sleep(0.5)
        lift.on_for_rotations(35, -0.8)
        #Turn to hit the helicopter
        my_tank.turn_degrees(10, -90, True, 1)
        init.debug_print("Turn to chopper" + str(my_tank.gyro.angle))
        #Navigation.gyro_check(my_tank, 10, -120)

        my_tank.on_for_rotations(15, 15, -0.195)


        my_tank.on_for_rotations(15, 15, 0.35)
        #target angle is -275

        my_tank.turn_degrees(10, 40, True, 1)
        my_tank.on_for_rotations(15, 15, 0.5)

        turn_angle = -1* (270 + (my_tank.gyro.angle))
        init.debug_print("Turned degrees" + str(turn_angle))
        my_tank.turn_degrees(10, turn_angle, True, 1)


Navigation.tank_init()
MediumMotor(OUTPUT_D)
claw.Claw()

def going_to_green(tank, lift, claw, slot=3, row=1):
    #start of code
    if slot == 3:
        x = 0
        tank.turn_degrees(10, -135, True, 1)
        init.debug_print("Going to green" + str(tank.gyro.angle))
        Navigation.distance_to_object(tank, 10, "Forward")
        tank.turn_degrees(10, -45, True, 1)
        Navigation.gyro_check(tank, 10, -180)
        init.debug_print("Going to forward to green" + str(tank.gyro.angle))
        claw.claw_open(100)
        lift.on_for_rotations(49, -2)
        Navigation.distance_to_object(tank, 25, "Forward")
        Navigation.gyro_check(tank, 10, -180)
        lift.on_for_rotations(49, 1.8)
        sleep(1)
        claw.claw_close(100)
        sleep(1)
        lift.on_for_rotations(49, -2)
        sleep(5)










def train(tank, Lift, claw):
    #init stuff
    init.debug_print("In train")
    my_tank = tank
    lift = Lift
    MyClaw = claw
    MyClaw.claw.reset()
    #lift.on_for_rotations(49, -3)
    my_tank.turn_degrees(10, 45, True, 1)
    return
    my_tank.on_for_rotations(20,20,0.2)
    my_tank.turn_degrees(10, -55, True, 1)
    sleep(1)
    my_tank.turn_degrees(10, 45, True, 1)
    my_tank.on_for_rotations(20, 20, 0.4)
    my_tank.turn_degrees(10, -45, True, 1)
    my_tank.on_for_rotations(20,20,-0.02)
    sleep(1)
    my_tank.on_for_rotations(20, 20, 0.07)
    my_tank.turn_degrees(10, 90, True, 1)
    init.debug_print("Turned degrees" + str(my_tank.gyro.angle))
    #init gyro var
    angle = my_tank.gyro.angle
    #compensate code
    if angle > 90:
        ofset1 = int(angle-90)
        my_tank.turn_degrees(10, int(ofset1), True, 1)
    elif angle < 90:
        ofset2 = int(90-angle)
        my_tank.turn_degrees(10, int(ofset2), True, 1)
    #bring claw down to move train
    lift.on_for_rotations(49, 2.3)
    #Chug the train
    Navigation.distance_to_object(my_tank, 47, "Forward")
    #lift.on_for_rotations(49,-1.3)
    MyClaw.claw_open(100)
    #pick up block
    sleep(1)
    lift.on_for_rotations(49,.4)
    #close claw
    MyClaw.claw_close(100)
    lift.on_for_rotations(49,-1)
    my_tank.on_for_rotations(10,10,-0.2)
    my_tank.turn_degrees(10,-55,True,1)
    sleep(1)
    MyClaw.claw_open(100)
    lift.on_for_rotations(10, -1)



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
    #blue_two_slot_one(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    going_to_green(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())



