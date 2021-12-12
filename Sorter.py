#!/usr/bin/env python3

import ev3dev.ev3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from time import sleep
import time
from ev3dev2.sound import Sound
import init
import claw
import Navigation
import truck


def current_run(tank, Lift, claw):
    x = 0
    init.debug_print("In current run")
    tank = tank
    lift = Lift
    MyClaw = claw
    MyClaw.claw.reset()
    lift.reset()
    tank.reset()
    #start of code
    lift.on_for_rotations(30, -1.5)
    tank.on_for_rotations(10, 10, 0.7)
    sleep(0.5)
    lift.on_for_rotations(10, 0.6)
    tank.on_for_rotations(15, 15, -0.7)
    sleep(0.5)
    lift.on_for_rotations(10, -0.3)
    MyClaw.claw_open(150)
    tank.turn_degrees(10, 90, True, 1)
    init.debug_print("Turned degrees to pick up brick" + str(tank.gyro.angle))
    tank.on_for_rotations(15, 15, -0.07 )
    #Goes down to pick up blue container
    lift.on_for_rotations(10, 1)
    MyClaw.claw.reset()
    if MyClaw.claw_close(100):
        init.debug_print("Found blue brick")
        sleep(1)
        lift.on_for_rotations(49, -3)
        tank.turn_degrees(10, -180, True, 1)

        Navigation.gyro_check(tank, 10, -90)
        init.debug_print("Turned degrees to turn to drop blue" + str(tank.gyro.angle))
        Navigation.distance_to_object(tank, 43, "Forward", 10 )
        lift.on_for_rotations(49, 3)
        sleep(1)
        MyClaw.claw_open(100)
        sleep(0.5)
        lift.on_for_rotations(35, -0.8)
        #Turn to hit the helicopter
        tank.turn_degrees(10, -90, True, 1)
        init.debug_print("Turn to chopper" + str(tank.gyro.angle))
        #Navigation.gyro_check(tank, 10, -120)

        tank.on_for_rotations(15, 15, -0.195)


        tank.on_for_rotations(15, 15, 0.35)
        #target angle is -275

        tank.turn_degrees(10, -90, True, 1)
        return
        tank.on_for_rotations(15, 15, 0.5)

        turn_angle = -1* (270 + (tank.gyro.angle))
        init.debug_print("Turned degrees" + str(turn_angle))
        tank.turn_degrees(10, turn_angle, True, 1)

def blue_two_slot_one(tank, lift, claw):
    x = 0
    init.debug_print("In blue two slot 1")
    #my_tank = tank
    #MyClaw = claw
    els = False

    claw.claw.reset()
    lift.reset()
    tank.reset()
    tank.gyro.reset()
    claw.claw_close(100)
    start_time = time.time()
    #start of code
    lift.on_for_rotations(30, -1.5)
    tank.on_for_rotations(10, 10, 0.7)
    sleep(0.5)
    lift.on_for_rotations(10, 0.6)
    tank.on_for_rotations(15, 15, -0.7)
    sleep(0.5)
    lift.on_for_rotations(10, -0.3)
    claw.claw_open(100)
    sleep(2)
    #claw.claw.reset()
    tank.turn_degrees(10, 90, True, 1)
    init.debug_print("Turned degrees to pick up brick" + str(tank.gyro.angle))
    tank.on_for_rotations(15, 15, -0.07 )
    #Goes down to pick up blue container
    lift.on_for_rotations(10, 1)
    #MyClaw.claw.reset()
    if claw.claw_close(100):
        init.debug_print("Found blue brick")
        lift.on_for_rotations(49, -0.5)
    else:
        claw.claw.reset()
        sleep(1)
        claw.claw_open(100)
        lift.on_for_rotations(49, -1)
        Navigation.distance_to_object(tank, 7.5, "Forward")
        lift.on_for_rotations(30, 1)
        claw.claw_close(100)
        lift.on_for_rotations(49, -0.5)
        Navigation.distance_to_object(tank, 7, "Backward")
    sleep(1)
    lift.on_for_rotations(49, -2)
    init.debug_print("After picking up blue" + str(tank.gyro.angle))
    #my_tank.turn_degrees(10,90)
    Navigation.gyro_check(tank, 10, 90)
    init.debug_print("Turned degrees to turn to drop blue" + str(tank.gyro.angle))
    #Navigation.distance_to_object(tank, 36, "Backward", 10)
    tank.on_for_rotations(-30, -30, 36/25.6353961)
    #Turn to Blue Circle
    tank.turn_degrees(10, 180, True, 1)
    Navigation.gyro_check(tank, 10, 270)
    init.debug_print("Dropping blue turn" + str(tank.gyro.angle))
    Navigation.distance_to_object(tank, 3, "Forward")
    sleep(0.5)
    lift.reset()
    lift.on_for_rotations(49, 1.7)
    sleep(0.5)
    claw.claw_open(100)
    sleep(0.5)
    lift.on_for_rotations(49, -1.7)
    Navigation.distance_to_object(tank, 15, "Backward")
    Navigation.gyro_check(tank, 10, 270)
    init.debug_print("Final turn " + str(tank.gyro.angle))
    tank.gyro.reset()
    init.debug_print("TIME: "+str(time.time()-start_time))
    return




def going_to_green(tank, lift, claw, slot=3, row=1):
    #start of code
    start_time2 = time.time()
    lift.on_for_rotations(49, 2)
    lift.reset()
    if slot == 3:
        x = 0
        lift.on_for_rotations(10, -0.3)
        claw.claw_open(100)
        sleep(1)
        tank.turn_degrees(10, -135, True, 1)
        init.debug_print("Going to green" + str(tank.gyro.angle))
        Navigation.distance_to_object(tank, 10.5, "Forward")
        tank.turn_degrees(10, -45, True, 1)
        Navigation.gyro_check(tank, 10, -180)

        init.debug_print("Going to forward to green" + str(tank.gyro.angle))
        lift.on_for_rotations(49, -2)
        #Navigation.distance_to_object(tank, 25, "Forward")
        tank.on_for_rotations(15, 15, 15.5/25.6353961)
        lift.reset()
        lift.on_for_rotations(49, 1.7)
        sleep(1)
        if claw.claw_close(100):
            sleep(1)
            lift.on_for_rotations(49, -2)
            sleep(0.5)
        else:
            lift.on_for_rotations(49, -2)
            claw.claw_open(100)
            sleep(1)

            Navigation.distance_to_object(tank, 7, "Forward")
            lift.on_for_rotations(49, 2)
            sleep(1)
            claw.claw_close(100)
            sleep(0.5)
            lift.on_for_rotations(49, -2)
            sleep(0.5)
            Navigation.distance_to_object(tank, 7, "Backward")

        Navigation.distance_to_object(tank, 1, "Backward")
        init.debug_print("Angle check" + str(tank.gyro.angle))
        tank.turn_degrees(10, 90, True, 1)
        #lift.on_for_rotations(49, 1.1)
        #sleep(0.5)
        #Navigation.distance_to_object(tank, 18, "Forward")
        #tank.on_for_rotations(20, 20, 18/25.6353961)
        #sleep(0.5)
        #Navigation.distance_to_object(tank, 15, "Backward")
        #tank.on_for_rotations(-20, -20, 15/25.6353961)
        #sleep(0.5)
        lift.on_for_rotations(49, 3)
        sleep(0.5)
        claw.claw_open(100)
        lift.on_for_rotations(49, -1)
        #Navigation.distance_to_object(tank, 5, "Backward")
        Navigation.gyro_check(tank, 10, -90)
        init.debug_print("TIME: "+str(time.time()-start_time2))
        tank.gyro.reset()

def going_to_green_other_side(tank, lift, claw, slot=3, row=1):
    #start of code
    start_time2 = time.time()
    lift.on_for_rotations(49, 2)
    lift.reset()
    if slot == 3:
        x = 0
        lift.on_for_rotations(49, -0.2)
        tank.turn_degrees(10, 135, True, 1)
        init.debug_print("Going to green" + str(tank.gyro.angle))
        Navigation.distance_to_object(tank, 18.5, "Forward")
        tank.turn_degrees(10, 45, True, 1)
        Navigation.gyro_check(tank, 10, 180)

        init.debug_print("Going to forward to green" + str(tank.gyro.angle))
        lift.on_for_rotations(49, -2)
        #Navigation.distance_to_object(tank, 25, "Forward")
        Navigation.distance_to_object(tank, 20, "Forward")
        lift.reset()
        Navigation.gyro_check(tank, 10, 180)
        lift.on_for_rotations(49, 1.7)
        sleep(1)
        if claw.claw_close(100):
            sleep(1)
            lift.on_for_rotations(49, -2)
            sleep(0.5)
            Navigation.distance_to_object(tank, 5, "Backward")
            init.debug_print("Angle check" + str(tank.gyro.angle))
            tank.turn_degrees(10, 90, True, 1)
            lift.on_for_rotations(49, 1.1)
            sleep(0.5)
            #Navigation.distance_to_object(tank, 18, "Forward")
            tank.on_for_rotations(20, 20, 30/25.6353961)
            sleep(0.5)
            #Navigation.distance_to_object(tank, 15, "Backward")
            tank.on_for_rotations(-20, -20, 27/25.6353961)
            sleep(0.5)
            lift.on_for_rotations(49, 0.6)
            sleep(0.5)
            claw.claw_open(100)
            lift.on_for_rotations(49, -1)
            Navigation.distance_to_object(tank, 5, "Backward")
            Navigation.gyro_check(tank, 10, -90)
            init.debug_print("TIME: "+str(time.time()-start_time2))
            tank.gyro.reset()






def test_claw(tank, lift, claw):

    claw.claw_open(150)
    sleep(2)
    claw.claw.reset()
    if claw.claw_close(100):
        init.debug_print("Caught Brick")
    else:
        init.debug_print("Not Caught")
    sleep(10)



def train(tank, Lift, claw):
    #init stuff
    init.debug_print("In train")
    tank = tank
    lift = Lift
    MyClaw = claw
    MyClaw.claw.reset()
    #lift.on_for_rotations(49, -3)
    tank.turn_degrees(10, 45, True, 1)
    return
    tank.on_for_rotations(20,20,0.2)
    tank.turn_degrees(10, -55, True, 1)
    sleep(1)
    tank.turn_degrees(10, 45, True, 1)
    tank.on_for_rotations(20, 20, 0.4)
    tank.turn_degrees(10, -45, True, 1)
    tank.on_for_rotations(20,20,-0.02)
    sleep(1)
    tank.on_for_rotations(20, 20, 0.07)
    tank.turn_degrees(10, 90, True, 1)
    init.debug_print("Turned degrees" + str(tank.gyro.angle))
    #init gyro var
    angle = tank.gyro.angle
    #compensate code
    if angle > 90:
        ofset1 = int(angle-90)
        tank.turn_degrees(10, int(ofset1), True, 1)
    elif angle < 90:
        ofset2 = int(90-angle)
        tank.turn_degrees(10, int(ofset2), True, 1)
    #bring claw down to move train
    lift.on_for_rotations(49, 2.3)
    #Chug the train
    Navigation.distance_to_object(tank, 47, "Forward")
    #lift.on_for_rotations(49,-1.3)
    MyClaw.claw_open(100)
    #pick up block
    sleep(1)
    lift.on_for_rotations(49,.4)
    #close claw
    MyClaw.claw_close(100)
    lift.on_for_rotations(49,-1)
    tank.on_for_rotations(10,10,-0.2)
    tank.turn_degrees(10,-55,True,1)
    sleep(1)
    MyClaw.claw_open(100)
    lift.on_for_rotations(10, -1)



def SlotToCircle(tank, lift, claw):
    #move to
    y = 0
    for i in range(3):
        tank.on_for_rotations(15, 15, 2)
        tank.on_for_rotations(15, 15, -2)
    y += 1
    lift.on_for_rotations(20,4)
    lift.on_for_rotations(-20,4)


def CircleToSlot():
    tank.on_for_rotations(15, 15, -0.75)
    tank.on_for_rotations(-15, 15, 0.5)
    tank.on_for_rotations(15, 15, 0.2)


def no_detection():
    claw.claw_open(100)
    lift.on_for_rotations(49, -3)
    tank.on_for_rotations(15, 15, 0.3)
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
    tank.on_for_rotations(15, 15, 0.4)
    MyClaw.claw_open(100)
    lift.on_for_rotations(49, 3)
    MyClaw.claw_close(100)
    lift.on_for_rotations(49, -3)

def end_game(tank, lift, claw):

    init.debug_print("we are in the endgame now")
    tank.gyro.reset()
    start_time = time.time()
    speed1 = 25
    lift.on_for_rotations(49, -2)
    tank.turn_degrees(10,90,True,1)
    Navigation.gyro_check(tank, 10, 90)
    tank.on_for_rotations(speed1,speed1,22 / 25.13)
    #Navigation.distance_to_object(tank, 20, "Forward",speed=10)
    tank.turn_degrees(10,-90,True,1)
    Navigation.gyro_check(tank, 10, 0)
    tank.on_for_rotations(speed1,speed1,66 / 25.13)
    #Navigation.distance_to_object(tank, 70, "Forward",speed=50)
    tank.turn_degrees(10,90,True,1)
    Navigation.gyro_check(tank, 10, 90)
    tank.on_for_rotations(speed1,speed1,30 / 25.13)

    #Navigation.distance_to_object(tank, 31, "Forward",speed=50)
    tank.turn_degrees(10,-90,True,1)
    Navigation.gyro_check(tank, 10, 0)
    Navigation.distance_to_object(tank, 19, "Forward", speed=5)

    init.debug_print("TIME: "+str(time.time()-start_time))

def completeRun (tank, lift, claw):
    truck.Innovate1(tank, lift, claw)
    blue_two_slot_one(tank, lift, claw)
    going_to_green(tank, lift, claw)
    end_game(tank, lift, claw)



if __name__ == "__main__":

    completeRun(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #blue_two_slot_one(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #going_to_green(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #end_game(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #test_claw(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #SlotToCircle(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())


