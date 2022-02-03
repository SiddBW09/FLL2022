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

def blue_two_slot_one2(tank, lift, claw):
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
    tank.on_for_rotations(10, 10, 0.6)
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
    Navigation.gyro_check(tank, 5, 90)
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

def going_to_green2(tank, lift, claw, slot=3, row=1):
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
        tank.on_for_rotations(15, 15, 15/25.6353961)
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
    sleep(1)
    tank.on_for_rotations(10, 10, 0.7)
    sleep(0.5)
    lift.on_for_rotations(10, 0.6)
    sleep(1)
    tank.on_for_rotations(15, 15, -0.7)
    sleep(0.5)
    lift.on_for_rotations(10, -0.3)
    sleep(1)
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
        Navigation.distance_to_object(tank, 7.5, "Backward")
    sleep(1)
    lift.on_for_rotations(49, -2)
    init.debug_print("After picking up blue" + str(tank.gyro.angle))
    #my_tank.turn_degrees(10,90)
    Navigation.gyro_check(tank, 10, 90)
    init.debug_print("Turned degrees to turn to drop blue" + str(tank.gyro.angle))
    #Navigation.distance_to_object(tank, 36, "Backward", 10)
    tank.on_for_rotations(-30, -30, 47/25.6353961)
    #Turn to Blue Circle
    tank.turn_degrees(10, 90, True, 1)
    Navigation.distance_to_object(tank, 10, "Backward")
    Navigation.distance_to_object(tank, 10, "Forward")
    tank.turn_degrees(10, 90, True, 1)
    Navigation.gyro_check(tank, 10, 270)
    init.debug_print("Dropping blue turn" + str(tank.gyro.angle))
    Navigation.distance_to_object(tank, 8, "Backward")
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

        lift.on_for_rotations(49, 2)
        sleep(1)
        #Navigation.distance_to_object(tank, 25, "Forward")
        tank.on_for_rotations(15, 15, 13/25.6353961)
        lift.reset()
        sleep(1)
        lift.on_for_rotations(49, -1.7)
        sleep(1)
        if claw.claw_close(100):
            sleep(1)
            lift.on_for_rotations(49, -2)
            sleep(0.5)
        '''else:
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
            Navigation.distance_to_object(tank, 7, "Backward")'''
        sleep(1)
        lift.on_for_rotations(49, -2)
        sleep(0.5)
        Navigation.distance_to_object(tank, 1, "Backward")
        init.debug_print("Angle check" + str(tank.gyro.angle))
        #goes to cargo ship
        tank.turn_degrees(10, 125, True, 1)
        tank.on_for_rotations(20, 20, 53/25.6353961)
        tank.turn_degrees(10, 55, True, 1)
        Navigation.distance_to_object(tank, 5, "Forward")
        #drops block on cargo ship
        lift.on_for_rotations(49, 1.1)
        sleep(1)
        claw.claw_open(100)
        Navigation.distance_to_object(tank, 5, "Backward")
        #lift.on_for_rotations(49, 1.1)
        #sleep(0.5)
        #Navigation.distance_to_object(tank, 18, "Forward")
        #tank.on_for_rotations(20, 20, 18/25.6353961)
        #sleep(0.5)
        #Navigation.distance_to_object(tank, 15, "Backward")
        #tank.on_for_rotations(-20, -20, 15/25.6353961)
        #sleep(0.5)
        #Navigation.gyro_check(tank, 10, -90)
        init.debug_print("TIME: "+str(time.time()-start_time2))
        tank.gyro.reset()

def blue_two_slot_one3(tank, lift, claw):
    x = 0
    init.debug_print("In blue two slot 1")
    #my_tank = tank
    #MyClaw = claw
    els = False
    #Starting: brickrun --directory="/home/robot/FLL2021" "/home/robot/FLL2021/main.py"
    claw.claw.reset()
    lift.reset()
    tank.reset()
    tank.gyro.reset()
    claw.claw_close(100)
    start_time = time.time()
    #start of code
    '''lift.on_for_rotations(30, -1.5)
    tank.on_for_rotations(10, 10, 0.7)
    sleep(0.5)
    lift.on_for_rotations(10, 0.6)
    tank.on_for_rotations(15, 15, -0.7)
    '''
    claw.claw_open(100)
    sleep(2)
    #claw.claw.reset()
    '''tank.turn_degrees(10, 90, True, 1)
    init.debug_print("Turned degrees to pick up brick" + str(tank.gyro.angle))
    tank.on_for_rotations(15, 15, -0.07 )
    #Goes down to pick up blue container'''
    lift.on_for_rotations(10, 0.5)
    claw.claw.reset()
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
        Navigation.distance_to_object(tank, 7.5, "Backward")
    sleep(1)
    lift.on_for_rotations(49, -2)
    init.debug_print("After picking up blue" + str(tank.gyro.angle))
    #my_tank.turn_degrees(10,90)
    Navigation.gyro_check(tank, 10, 0)
    init.debug_print("Turned degrees to turn to drop blue" + str(tank.gyro.angle))
    #Navigation.distance_to_object(tank, 36, "Backward", 10)
    tank.on_for_rotations(-30, -30, 47/25.6353961)
    #Turn to Blue Circle
    tank.turn_degrees(10, 90, True, 1)
    Navigation.distance_to_object(tank, 10, "Backward")
    Navigation.distance_to_object(tank, 10, "Forward")
    tank.turn_degrees(10, 90, True, 1)
    Navigation.gyro_check(tank, 10, 180)
    init.debug_print("Dropping blue turn" + str(tank.gyro.angle))
    Navigation.distance_to_object(tank, 8, "Backward")
    sleep(0.5)
    lift.reset()
    lift.on_for_rotations(49, 1.7)
    sleep(0.5)
    claw.claw_open(100)
    sleep(0.5)
    lift.on_for_rotations(49, -1.7)
    Navigation.distance_to_object(tank, 15, "Backward")
    Navigation.gyro_check(tank, 10, 180)
    init.debug_print("Final turn " + str(tank.gyro.angle))
    tank.gyro.reset()
    init.debug_print("TIME: "+str(time.time()-start_time))
    return

def lift_check (tank, lift):
    lift.on_for_rotations(20, 6)
    lift.on_for_rotations(0, -6)

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
        Navigation.distance_to_object(tank, 17, "Forward")
        tank.turn_degrees(10, 45, True, 1)
        Navigation.gyro_check(tank, 10, 180)

        init.debug_print("Going to forward to green" + str(tank.gyro.angle))
        lift.on_for_rotations(49, -2)
        #Navigation.distance_to_object(tank, 25, "Forward")
        Navigation.distance_to_object(tank, 19, "Forward")
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
            tank.turn_degrees(10, 30, True, 1)
            lift.on_for_rotations(49, 6)
            claw.claw_open(100)

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

def test_claw(tank, lift, MyClaw):
    Navigation.distance_goer(tank, 100, 30, 0)
    """MyClaw.claw_open(100)
    sleep(1)
    MyClaw.claw_close_5()"""

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
    truck.Innovate3(tank, lift, claw)
    blue_two_slot_one(tank, lift, claw)
    going_to_green(tank, lift, claw)
    #end_game(tank, lift, claw)

def GoingtoSorter(tank, lift, Claw):

    start_time = time.time()

    import claw


    #tank = Navigation.tank_init()
    #lift = MediumMotor(OUTPUT_D)
    #Claw = claw.Claw()
    tank.gyro.reset()

    #claw.claw_close(100)
    #sleep(1)
    #lift.on_for_rotations(30, -4)
    #sleep(5)
    #return


    lift.reset()
    Claw.claw_close_5()
    sleep(1)
    lift.on_for_rotations(35, -0.25)
    #Navigation.distance_to_object(tank, 92, "Backward", 10)
    #Navigation.new_move_incm(tank, -30, 92)
    Navigation.distance_goer(tank, 100, -50, 0)


    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))
    return
    #Do bridge mission
    tank.turn_degrees(10, 180, True, 1)
    Navigation.gyro_check(tank, 10, 180)

    init.debug_print("The amount turned before check: " + str(tank.gyro.angle))
    Navigation.gyro_check(tank, 10, 180)
    #Navigation.distance_to_object(tank, 28, "Forward", 15)
    #Navigation.new_move_incm(tank, 25, 28)
    Navigation.distance_goer(tank, 25, 28, 180)
    Navigation.gyro_check(tank, 10, 180)

    return
    #(Curr angle should be 90)
    #Navigation.distance_to_object(tank, 5, "Forward", 15)
    Navigation.distance_goer(tank, 5, 15, 90)

    tank.turn_degrees(10, -42, True, 1)
    tank.turn_degrees(10, 42, True, 1)
    #Navigation.distance_to_object(tank, 1, "Forward", 15)
    Navigation.distance_goer(tank, 1, 15, 42)
    #Dropping innovation piece.
    lift.on_for_rotations(30, 2)
    sleep(0.5)
    Claw.claw_open(100)
    sleep(0.5)
    lift.on_for_rotations(30, -3)
    #Navigation.distance_to_object(tank, 1, "Backward", 15)
    Navigation.distance_goer(tank, 1, -15, 90)
    tank.turn_degrees(10, 40, True, 1)

    #Going Forward after supply drop
    #Navigation.distance_to_object(tank, 15, "Forward", 15)
    Navigation.distance_goer(tank, 15, speed, angle)

    tank.turn_degrees(10, 60, True, 1)
    Navigation.gyro_check(tank, 5, 180)


    #Navigation.distance_to_object(tank, 18, "Forward", 15)
    Navigation.distance_goer(tank, 18, 15, 180)

    Navigation.gyro_check(tank, 5, 180)

    init.debug_print("Final angle is:" + str(tank.gyro.angle))
    #this is where we are, sid can continue tomorrow

    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))
    return


    tank.on_for_rotations(10, 0, 0.75)
    Navigation.gyro_check(tank, 5, 180)
    Navigation.distance_to_object(tank, 21.5, "Forward")
    lift.on_for_rotations(20,4)
    lift.reset()



    """tank.turn_degrees(10, 47, True, 1)
    Navigation.gyro_check(tank, 5, 47)
    Navigation.distance_to_object(tank, 45, "Backward", 10)
    Navigation.gyro_check(tank, 5, 48)
    tank.turn_degrees(10, -60, True, 1)
    tank.turn_degrees(10, 60, True, 1)"""
    #lift.on_for_rotations(30, 2)
    #tank.turn_degrees(10, 90, True, 1)
    #Navigation.gyro_check(tank, 25, 90)
    #Navigation.distance_to_object(tank, 89.5, "Backward", 10)

def motor_check(speed, rotations, lift_motor):
    if 'stalled' in lift_motor.state:
        lift_motor.reset()
        lift_motor.on_for_rotations(speed, rotations, brake=True)
    else:
        lift_motor.on_for_rotations(speed, rotations, brake=True)

def NewIdea(tank, lift, Claw):


    start_time = time.time()
    import claw
    tank.gyro.reset()
    lift.reset()

    #Going to Cargo Connect Circle
    #first bridge
    Navigation.distance_goer(tank, 99, -40, 0)

    sleep(1)
    lift.on_for_rotations(30, -1)
    #second bridge
    Navigation.distance_goer(tank, 18.4, -20, 0) #OG val 19
    Navigation.gyro_check(tank, 5, 0)
    lift.on_for_rotations(30, 1)
    Navigation.distance_goer(tank, 8, 20, 0)
    lift.on_for_rotations(30, -1.5)
    #innovation project in circle
    Navigation.distance_goer(tank, 7, -20, 0)
    tank.turn_degrees(15, -75)
    Navigation.distance_goer(tank, 8, -10, -75)
    Navigation.distance_goer(tank, 5, 10, -75)
    tank.turn_degrees(5, -12.5)
    #working perfectly until now
    Navigation.distance_goer(tank, 1, 15, -95)
    tank.turn_degrees(10, -138)

    Navigation.distance_goer(tank, 12, 25, -229)
    Navigation.gyro_check(tank, 5, -214)

    #Go to train
    Navigation.distance_goer(tank, 10, 20, -214)
    Navigation.gyro_check(tank, 5, -180)
    Navigation.distance_goer(tank, 31, 20, -180)
    sleep(0.5)



    lift.on_for_rotations(30, 0.75)
    Navigation.distance_goer(tank, 16, -20, -180)
    init.debug_print("Angle 1 "+str(tank.gyro.angle))
    #tank.turn_degrees(10, 9, True, 1) WTF is that??? -Coach
    #Navigation.gyro_check(tank, 10.9, -90) Why the duck did you use such a number?? -Coach/Wordsmithed by Sunny S
    Navigation.gyro_check(tank, 5, -90)
    lift.on_for_rotations(30, -0.75)

    sleep(1)
    Navigation.gyro_check(tank, 5, -90)
    init.debug_print("Angel"+str(tank.gyro.angle))
    #Navigation.gyro_check(tank, 5, -90)


    init.debug_print("New Idea Time: "+str(time.time()-start_time))
    #Navigation.gyro_check(tank, 10, -90)
    return
    pickupgreen(tank, lift, Claw, start_time, 2)
    #Navigation.distance_goer(tank, 3, 5, 0)


    #Sorter1(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())

def NewerIdea(tank, lift, Claw):
    start_time = time.time()
    import claw
    tank.gyro.reset()
    lift.reset()

    #Going to Cargo Connect Circle
    #first bridge
    Navigation.distance_goer(tank, 99, -40, 0)

    sleep(1)
    lift.on_for_rotations(30, -1)
    #second bridge
    Navigation.distance_goer(tank, 18.4, -20, 0) #OG val 19
    Navigation.gyro_check(tank, 5, 0)
    lift.on_for_rotations(30, 1)
    Navigation.distance_goer(tank, 8, 20, 0)
    lift.on_for_rotations(30, -1.5)
    #innovation project in circle
    Navigation.distance_goer(tank, 7, -20, 0)
    Navigation.gyro_check(tank, 5, -75)
    Navigation.distance_goer(tank, 8, -10, -75)
    Navigation.distance_goer(tank, 5, 10, -75)
    Navigation.gyro_check(tank, 5, -95)
    #working perfectly until now
    Navigation.distance_goer(tank, 5, 15, -95)
    Navigation.gyro_check(tank, 5, -230)


    Navigation.distance_goer(tank, 50, 25, -230)
    Navigation.gyro_check(tank, 5, -90)

    #Go to sorty
    Navigation.distance_goer(tank, 19.5, 25, -90)
    Navigation.gyro_check(tank, 5, -90)
    sleep(1)
    Navigation.gyro_check(tank, 2, -90)
    Navigation.gyro_check(tank, 2, -90)


    pickupgreen(tank, lift, Claw, start_time, 2)



def pickupbluebrick(tank, lift, MyClaw, time, slot):

    start_time = time.time()
    tank.gyro.reset()
    lift.reset()
    #import claw
    Navigation.distance_goer(tank, 2, 5, 0)
    MyClaw.claw_open(100)
    lift.on_for_rotations(30, 2)
    if ("caught brick" == MyClaw.claw_close_5()):
        lift.on_for_rotations(30, -1)
        sleep(0.5)
        Navigation.distance_goer(tank, 45, -20, 0)
        tank.turn_degrees(15, -180, True, 1)
        lift.on_for_rotations(30, 0.4)
        MyClaw.claw_open(100)

def pickupgreen(tank, lift, MyClaw, last_time, slot):
    start_time = last_time
    tank.gyro.reset()
    lift.reset()
    motor_check(50, -3, lift)

    speed = 10

    if slot == 2:
        #import claw
        MyClaw.claw_open(100)
        motor_check(30, 1.9, lift)

        if MyClaw.claw_close_5() == "caught brick":
            sleep(1)
            motor_check(30, -1, lift)
            #tank.turn_degrees(15, 90, True, 1)
            Navigation.gyro_check(tank, speed, 90)
            Navigation.distance_goer(tank, 10, 20, 90)
            motor_check(50, 1, lift)
            MyClaw.claw_open(100)
            motor_check(60, -4, lift)
            # sleep(0.5)
            # motor_check(50, -1, lift)
            # Navigation.distance_goer(tank, 11, -20, 90)
            Navigation.gyro_check(tank, speed, 0)
            sleep(0.5)
            Navigation.gyro_check(tank, 5, 0)


            init.debug_print("PickUpGreen: "+str(time.time()-start_time))

            blue1(tank, lift, MyClaw, start_time, 1)
        else:
            motor_check(50, -3, lift)
            pickupgreen(tank, lift, MyClaw, start_time, 1)

    if slot == 1:
        MyClaw.claw_open(100)
        motor_check(50, -1.8, lift)

        #Go to brick
        Navigation.gyro_check(tank, speed, 90)
        Navigation.distance_goer(tank, 11, 20, 90)
        sleep(0.5)
        Navigation.gyro_check(tank, speed, 0)
        init.debug_print("Angle Before Going and Picking Green Brick: "+str(tank.gyro.angle))

        #Pick up
        motor_check(50, 3, lift)

        if MyClaw.claw_close_5() == "caught brick" :
            sleep(1)
            init.debug_print("Got a Green brick")
            motor_check(30, -1, lift)

            #Drop at circle
            Navigation.gyro_check(tank, speed, 90)

            motor_check(50, 0.8, lift)
            MyClaw.claw_open(100)
            motor_check(50, -1, lift)

            #Go back to home
            Navigation.distance_goer(tank, 9, -20, 90)
            #tank.turn_degrees(10, 90, True, 1)
            sleep(0.5)
            Navigation.gyro_check(tank, speed, 0)

            blue1(tank, lift, MyClaw, start_time, 2)
            init.debug_print("PickUpGreen: "+str(time.time()-start_time))



def blue1(tank, lift, MyClaw, last_time, slot):
    start_time = last_time
    tank.gyro.reset()
    lift.reset()
    motor_check(50, -4, lift)
    MyClaw.claw_open(100)

    speed = 10

    if slot == 1:
        # #Go to brick
        # Navigation.gyro_check(tank, speed, 90)
        # Navigation.distance_goer(tank, 11, 20, 90)
        # Navigation.gyro_check(tank, speed, 0)
        # init.debug_print("Angle Before Going and Picking BLue Brick: "+str(tank.gyro.angle))
        Navigation.distance_goer(tank, 8, 10, 0)
        #tank.turn_degrees(10, 0-tank.gyro.angle)
        #Navigation.gyro_check(tank, speed, 0)
        #sleep(0.5)
        #Navigation.gyro_check(tank, speed, 0)
        motor_check(50, 2, lift)

        if MyClaw.claw_close_5() == "caught brick":
            sleep(1)
            init.debug_print("Caught Blue Brick!")
            motor_check(50, -3, lift)
            sleep(0.5)
            Navigation.gyro_check(tank, speed, 0)
            Navigation.distance_goer(tank, 22, -10, 0)
            Navigation.gyro_check(tank, speed, -90)
            Navigation.distance_goer(tank, 8, 20, -90)
            Navigation.gyro_check(tank, speed, -180)
            #Navigation.distance_goer(tank, 6, 10, -180)
            bluebrick_chopper(tank, lift, MyClaw, last_time)
            init.debug_print("The time after blue chopper:" + str(time.time()))


        else:
            motor_check(50, -3, lift)
            sleep(0.5)
            Navigation.gyro_check(tank, speed, 0)
            Navigation.distance_goer(tank, 8, -10, 0)
            Navigation.gyro_check(tank, speed, 90)
            Navigation.distance_goer(tank, 11, -20, 90)
            Navigation.gyro_check(tank, speed, 90)
            Navigation.gyro_check(tank, speed, 0)

            blue1(tank, lift, MyClaw, start_time, 3)


    if slot == 2:
        Navigation.distance_goer(tank, 8.5, 10, 0)
        motor_check(50, 2.3, lift)

        if MyClaw.claw_close_5():
            sleep(1)
            motor_check(-50, 3, lift)
            Navigation.distance_goer(tank, 8.5, -10, 0)

            #Going into posistion for next function
            Navigation.gyro_check(tank, speed, -180)
            Navigation.distance_goer(tank, 8, -10, -180)
            Navigation.gyro_check(tank, speed, -180)
            sleep(0.5)
            Navigation.gyro_check(tank, speed, -180)
            init.debug_print("BluePickUp: "+str(time.time()-start_time))
            bluebrick_chopper(tank, lift, MyClaw, start_time)
        else:
            sleep(1)
            motor_check(-50, 3, lift)
            Navigation.distance_goer(tank, 8.5, -10, 0)
            blue1(tank, lift, MyClaw, start_time, 3)

    if slot == 3:
        init.debug_print("Goin to slot 3!")

        #Go to brick
        Navigation.gyro_check(tank, speed, -90)
        Navigation.distance_goer(tank, 9, 20, -90)
        Navigation.gyro_check(tank, speed, 0)
        Navigation.distance_goer(tank, 8, 10, 0)
        Navigation.gyro_check(tank, speed, 0)
        sleep(0.5)
        Navigation.gyro_check(tank, speed, 0)
        motor_check(50, 2, lift)

        if MyClaw.claw_close_5() == "caught brick":
            #This is noob coach loser idea.
            sleep(0.5)
            init.debug_print("Caught Blue Brick!")
            motor_check(50, -3, lift)
            sleep(0.5)
            Navigation.gyro_check(tank, speed, 0)
            Navigation.distance_goer(tank, 8, -10, 0)
            Navigation.gyro_check(tank, speed, -90)
            Navigation.distance_goer(tank, 8.5, -10, -90)
            Navigation.gyro_check(tank, speed, -90)





        #Going into posistion for next function
        Navigation.gyro_check(tank, speed, -180)
        Navigation.distance_goer(tank, 8, -10, -180)
        Navigation.gyro_check(tank, speed, -180)
        sleep(0.5)
        Navigation.gyro_check(tank, speed, -180)
        init.debug_print("BluePickUp: "+str(time.time()-start_time))
        bluebrick_chopper(tank, lift, MyClaw, start_time)



def bluebrick_chopper(tank, lift, MyClaw, last_time):
    start_time = last_time
    speed = 10


    #Drop Blue Brick from Middle Collum
    #tank.gyro.reset()
    #Samarth Changes: We are doing this because this function expects us to be in a certain position which doesn't work with the changes we made before.
    #Navigation.gyro_check(tank, speed, -180)
    #sleep(0.5)
    #Navigation.gyro_check(tank, speed, -180)
    Navigation.distance_goer(tank, 27, 15, -180)
    Navigation.gyro_check(tank, speed, -180)
    motor_check(50, 2, lift)
    MyClaw.claw_open(100)
    Navigation.gyro_check(tank, speed, -180)



    #Turn and do Chopper
    motor_check(50, -3.5, lift)
    Navigation.distance_goer(tank, 3, -10, -180)
    Navigation.gyro_check(tank, speed, -290)
    Navigation.distance_goer(tank, 14, -15, -290)
    Navigation.gyro_check(tank, speed, -290)
    Navigation.distance_goer(tank, 20, 25, -290)


    tank.reset()

    #Go and do Cargo Ship
    Navigation.gyro_check(tank, speed, -270)
    sleep(0.5)
    Navigation.gyro_check(tank, speed, -270)
    Navigation.distance_goer(tank, 24, 20, -270)
    motor_check(50, 4, lift)
    sleep(0.5)
    Navigation.distance_goer(tank, 14, -16, -270)
    Navigation.distance_goer(tank, 12.5, 16, -270)
    motor_check(50, -2, lift)



    #Go to Speed Bump
    Navigation.distance_goer(tank, 31, 28, -270)
    Navigation.gyro_check(tank, speed, -225)
    Navigation.distance_goer(tank, 28, 30, -225)
    Navigation.gyro_check(tank, speed, -210)
    motor_check(30, 1, lift)
    sleep(0.5)
    Navigation.gyro_check(tank, 5, -290)
    #everything works except for the speed bump and we have to do combo 3


    init.debug_print(tank.gyro.angle)
    #last lefo of
    init.debug_print("Total Time: "+str(time.time()-start_time))





if __name__ == "__main__":
    #truck.Innovate1(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #GoingtoSorter(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())

    NewerIdea(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #pickupbluebrick(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #completeRun(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #blue_two_slot_one(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #lift_check(Navigation.tank_init(), MediumMotor(OUTPUT_D))
    #going_to_green(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #end_game(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #test_claw(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #SlotToCircle(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #pickupgreen(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw(), time.time(), slot = 2)
    #blue1(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())


