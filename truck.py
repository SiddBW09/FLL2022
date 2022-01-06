#!/usr/bin/env python3
import ev3dev.ev3
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, MoveTank, SpeedPercent, follow_for_ms, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import Navigation
import time
from time import sleep
from ev3dev2.motor import OUTPUT_B, MediumMotor
import init
import claw

def Code():
    tank = Navigation.tank_init()
    lift = MediumMotor(OUTPUT_D)
    Claw = claw.Claw()
    tank.gyro.reset()


    #tank.turn_degrees(10, -180, True, 1)
    #Navigation.gyro_check(tank, 20, -180)
    Navigation.distance_to_object(tank, 21, "Forward")
    tank.turn_degrees(10, -90, True, 1)

    Navigation.gyro_check(tank, 20, -90)
    Navigation.distance_to_object(tank, 20, "Forward")
    tank.turn_degrees(10, -90, True, 1)


def Innovate(tank, lift, claw):

    start_time = time.time()

    import claw


    tank = Navigation.tank_init()
    lift = MediumMotor(OUTPUT_D)
    Claw = claw.Claw()
    tank.gyro.reset()

    #claw.claw_close(100)
    #sleep(1)
    #lift.on_for_rotations(30, -4)
    #sleep(5)
    #return


    lift.reset()
    Claw.claw_close(100)
    sleep(0.5)
    lift.on_for_rotations(35, -0.5)
    #Navigation.distance_to_object(tank, 92, "Backward", 10)
    Navigation.new_move_incm(tank, -30, 92)

    #Do bridge mission
    tank.turn_degrees(10, 100, True, 1)
    tank.turn_degrees(10, -100, True, 1)
    Navigation.gyro_check(tank, 20, 0)

    init.debug_print("The amount turned before check: " + str(tank.gyro.angle))
    Navigation.gyro_check(tank, 10, 0)
    Navigation.distance_to_object(tank, 27, "Backward")
    gyro_check(tank, 0)

    tank.turn_degrees(10, -90, True, 1)
    gyro_check(tank, -90)
    #(Curr angle should be -90)
    Navigation.distance_to_object(tank, 10, "Backward")
    tank.on_for_rotations(0, -10, 0.5)
    #Go to logo
    #Navigation.distance_to_object(tank, 45, "Backward", 10)

    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))

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


def Innovate1(tank, lift, Claw):

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
    Claw.claw_close(100)
    sleep(0.5)
    lift.on_for_rotations(35, -0.8)
    #Navigation.distance_to_object(tank, 92, "Backward", 10)
    Navigation.new_move_incm(tank, -25, 92)

    #Do bridge mission
    tank.turn_degrees(10, 180, True, 1)
    Navigation.gyro_check(tank, 10, 180)
    #tank.turn_degrees(10, -100, True, 1)

    init.debug_print("The amount turned before check: " + str(tank.gyro.angle))
    Navigation.gyro_check(tank, 10, 180)
    Navigation.distance_to_object(tank, 28, "Forward", 15)

    tank.turn_degrees(10, -90, True, 1)
    Navigation.gyro_check(tank, 10, 90)
    #(Curr angle should be -90)
    Navigation.distance_to_object(tank, 11, "Forward", 15)


    tank.turn_degrees(10, -60, True, 1)
    tank.turn_degrees(10, 30, True, 1)
    Claw.claw_open(100)
    tank.turn_degrees(10, 30, True, 1)


    tank.on_for_rotations(10, 0, 0.75)
    Navigation.gyro_check(tank, 5, 180)
    Navigation.distance_to_object(tank, 21.5, "Forward")
    lift.on_for_rotations(20,4)
    lift.reset()

    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))

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


def turn_right(tank, angle): #Function which accurately turns the robot 90 degrees to the right.
    #tank.turn_right(20, angle-20)
    gyroangle = tank.gyro.angle
    offset = (angle - gyroangle)

    #Printing values to check the angles.
    #time.sleep(1)
    init.debug_print("Amount of degrees turned: " + str(gyroangle))
    init.debug_print("The offset is: " + str(offset))

    #First offset check to get the robot to near 90, since we start with turning less degrees.
    if offset > 0:
        offset1 = (offset * -1)
        tank.turn_right(10, offset1)
    elif offset < 0:
        tank.turn_left(10, offset)

    angle_after_turn = tank.gyro.angle
    init.debug_print("Angle (after 1 offset check): " + str(angle_after_turn))

    #Second offset check (slower) to fine-tune the angle.
    offset = angle-angle_after_turn
    if offset > 0:
        offset1 = (offset * -1)
        tank.turn_right(7, offset1)
    elif offset < 0:
        tank.turn_left(7, offset)

    init.debug_print("Final angle is: " + str(tank.gyro.angle))
    init.debug_print("-------------------------------------")


def turn_left(tank, angle): #Functions which accurately turns the robot 90 degrees to the right.'''
    #tank.gyro.reset()
    #tank.turn_left(20, angle-20)
    gyroangle = tank.gyro.angle

    offset = (angle - gyroangle)

    #Printing values to check the angles.
    time.sleep(1)
    init.debug_print("Amount of degrees turned: " + str(gyroangle))
    #init.debug_print("The offset is: " + str(offset))
    #First offset check to get the robot to near 90, since we start with turning less degrees.
    if offset > 0:
        offset1 = (offset * -1)
        tank.turn_left(10, offset1)
    elif offset < 0:
        tank.turn_right(10, offset)
        angle_after_turn = tank.gyro.angle
        init.debug_print("Angle (after 1 offset check): " + str(angle_after_turn))

    #Second offset check (slower) to fine-tune the angle.
        offset = angle-angle_after_turn
        if offset > 0:
            offset1 = (offset * -1)
            tank.turn_left(7, offset1)
        elif offset < 0:
            tank.turn_right(7, offset)


    init.debug_print("Final angle is: " + str(tank.gyro.angle))
    init.debug_print("-------------------------------------")

def truck_2():
    #Initializing tank
    tank = Navigation.tank_init()
    lift = MediumMotor(OUTPUT_D)
    tank.gyro.reset()
    # Init Color Sensors

    #truck_to_bridge(tank, lift)
    #return

    colorRight = ColorSensor(INPUT_2)
    colorLeft = ColorSensor(INPUT_3)
    start_time = time.time()

    #turn_right(tank, 45)
    #tank.turn_degrees(10, 45, True, 2)
    init.debug_print("First 45 degrees turned:" + str(tank.gyro.angle))
    Navigation.distance_to_object(tank, 41.595, "Backward")
    """tank.turn_degrees(10, 40, True, 2)
    #init.debug_print(str(tank.gyro.angle))
    Navigation.distance_to_object(tank, 29, "Backward")
    tank.turn_degrees(10, 90, True, 2)

    angle_now = tank.gyro.angle
    init.debug_print("90 angle: " + str(angle_now))
    #return
    if angle_now > 90:
        #Turn angle-90 to the left
        offset1 = int(angle_now-90)
        tank.turn_degrees(10, -1*(offset1), True, 1)
        init.debug_print("Final angle turned: " + str(angle_now - offset1))
    elif angle_now < 90:
        #Turn 90-angle to the right
        offset2 = int(90-angle_now)
        tank.turn_degrees(10, int(offset2), True, 1)
        init.debug_print("Final angle turned: " + str(angle_now - offset2))"""
    turn_right(tank, 90)
    Navigation.distance_to_object(tank, 23, "Backward") #Push trucks together.
    Navigation.distance_to_object(tank, 17, "Forward") #Back up from trucks.
    return

    tank.turn_degrees(10, -45, True, 1)
    angle_now = tank.gyro.angle
    init.debug_print("Angle (after 1 offset check): " + str(angle_now))
    if angle_now < 45:
        #Turn angle-90 to the left
        offset1 = int(angle_now-45)
        tank.turn_degrees(10, -int(offset1), True, 1)
        init.debug_print("Final angle turned: " + str(angle_now - offset1))
    elif angle_now > 45:
        #Turn 90-angle to the right
        offset2 = int(45-angle_now)
        tank.turn_degrees(10, int(offset2), True, 1)
        init.debug_print("Final angle turned: " + str(angle_now - offset2))
    Navigation.distance_to_object(tank, 27, "Backward")
    #lift.on_for_rotations(-20, 1)

    tank.turn_degrees(10, 45, True, 1) #Parallel to trucks.

    """angle_now = tank.gyro.angle
    init.debug_print("Angle (after 1 offset check): " + str(angle_now))
    if angle_now < 45:
        #Turn angle-90 to the left
        offset1 = int(angle_now-45)
        Navigation.turn_degrees(tank, int(offset1), "Left")
        init.debug_print("Final angle turned: " + str(angle_now - offset1))
    elif angle_now > 45:
        #Turn 90-angle to the right
        offset2 = int(45-angle_now)
        Navigation.turn_degrees(tank, int(offset2), "Right")
        init.debug_print("Final angle turned: " + str(angle_now - offset2))"""
    truck_to_bridge(tank, lift)
    Navigation.distance_to_object(tank, 8, "Backward")
    Navigation.turn_degrees(tank, 85, "Left")
    angle_now = tank.gyro.angle
    init.debug_print("Angle (after 1 offset check): " + str(angle_now))
    if angle_now < 85:
        #Turn angle-90 to the left
        offset1 = int(angle_now-85)
        Navigation.turn_degrees(tank, int(offset1), "Left")
        init.debug_print("Final angle turned: " + str(angle_now - offset1))
    elif angle_now > 85:
        #Turn 90-angle to the right
        offset2 = int(85-angle_now)
        Navigation.turn_degrees(tank, int(offset2), "Right")
        init.debug_print("Final angle turned: " + str(angle_now - offset2))
    Navigation.distance_to_object(tank, 20, "Backward")

    #turn_right(tank, 45)
    #init.debug_print("The amount of degrees turned is: " + str(tank.gyro.angle))
    #init.debug_print("The amount of degrees used to offset: " + str(90 - tank.gyro.angle))
    #Navigation.distance_to_object(tank, 20, "Backward")
    #Navigation.distance_to_object(tank, 18, "Forward")
    #turn_left(tank, 50)
    #Navigation.distance_to_object(tank, 13.5, "Backward")
    #turn_left(tank, 85)
    #Navigation.distance_to_object(tank, 20, "Backward")

def truck_to_bridge (tank, lift):
    tank.gyro.reset()
    lift.on_for_rotations(-20, 0.48)

    Navigation.distance_to_object(tank, 40, "Backward")
    tank.turn_degrees(20, -190, True, 1)
    tank.on_for_rotations(10, 10, 0.58)
    turn_right(tank, 0)
    tank.on_for_rotations(10, 10, 0.4)
    tank.turn_degrees(20, 60, True, 1)
    #tank.turn_degrees(20, -35, True, 1)
    init.debug_print(tank.gyro.angle)

    tank.turn_degrees(20, )
    return


    Navigation.distance_to_object(tank, 30, "Forward")
    Navigation.turn_degrees(tank, 180, "Right")
    init.debug_print(tank.gyro.angle)
    """Navigation.distance_to_object(tank, 65, "Backward")
    lift.on_for_rotations(-30, 0.5)
    Navigation.distance_to_object(tank, 9, "Backward")
    lift.on_for_rotations(30, 0.6)
    Navigation.distance_to_object(tank, 13, "Forward")
    Navigation.distance_to_object(tank, 40, "Backward")"""

def gyro_check (tank, angle):
    angle_now = tank.gyro.angle
    if angle_now > angle:
        #Turn angle-90 to the left
        offset1 = angle_now-angle
        tank.turn_degrees(10, -1*(offset1), True, 1)
        init.debug_print("Final angle turned: " + str(tank.gyro.angle))
    elif angle_now < angle:
        #Turn 90-angle to the right
        offset2 = angle-angle_now
        tank.turn_degrees(10, offset2, True, 1)
        init.debug_print("Final angle turned: " + str(tank.gyro.angle))

def truck_3(tank, lift, Claw): #Working, final version.
    #Initializing tank
    #tank = Navigation.tank_init()
    tank.gyro.reset()
    #Claw = claw.Claw()
    start_time = time.time()

    #Gyro Testing Sequence
    '''init.debug_print(tank.gyro.angle)
    tank.on_for_rotations(-10, -10, 0.5)
    init.debug_print(tank.gyro.angle)
    tank.on_for_rotations(-10, -10, 1)
    sleep(1)
    init.debug_print(tank.gyro.angle)
    return'''

    forward_distance_to_trucks = 31/25.6353961
    tank.on_for_rotations(-10, -10, forward_distance_to_trucks)
    gyro_check(tank, 0)
    init.debug_print("Angle after going forward from home: " + str(tank.gyro.angle))

    #Turn to trucks.
    tank.turn_degrees(10, 90, True, 1)
    gyro_check(tank, 90)
    init.debug_print("90 degrees turn is: " + str(tank.gyro.angle))

    #Push and back out of trucks.
    #Navigation.distance_to_object(tank, 11, "Backward")
    forward_distance = 26/25.6353961
    tank.on_for_rotations(-10, -10, forward_distance)
    init.debug_print("The gyro angle after forward part 1: " + str(tank.gyro.angle))
    gyro_check(tank, 90)
    tank.on_for_rotations(-10, -10, 27.35/25.6353961)
    tank.on_for_rotations(10, 10, 20/25.6353961)

    #GO HOME! DONE WITH MISSION!
    tank.turn_degrees(10, -30, True, 1)
    distance_to_home = 40/25.6353961
    tank.on_for_rotations(40, 40, distance_to_home)

    Claw.claw_open(100)

    '''
    endtime1 = int(time.time()-start_time)
    init.debug_print(endtime1)
    '''
    lift.on_for_rotations(49, 3)
    lift.reset()
    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))

def Innovate2(tank, lift, Claw):

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
    Claw.claw_close(100)
    sleep(0.5)
    lift.on_for_rotations(35, -0.9)
    #Navigation.distance_to_object(tank, 92, "Backward", 10)
    Navigation.new_move_incm(tank, -25, 45)
    Navigation.gyro_check(tank, 10, 0)
    Navigation.new_move_incm(tank, -25, 47)
    Navigation.gyro_check(tank, 10, 0)

    #Do bridge mission
    tank.turn_degrees(10, 180, True, 1)
    Navigation.gyro_check(tank, 10, 180)
    #tank.turn_degrees(10, -100, True, 1)

    init.debug_print("The amount turned before check: " + str(tank.gyro.angle))
    Navigation.gyro_check(tank, 10, 180)
    Navigation.distance_to_object(tank, 28, "Forward", 15)

    tank.turn_degrees(10, -90, True, 1)
    Navigation.gyro_check(tank, 10, 90)
    #(Curr angle should be -90)
    tank.on_for_rotations(15, 15, -1)
    Navigation.distance_to_object(tank, 33, "Forward", 15)


    tank.turn_degrees(10, -90, True, 1)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.distance_to_object(tank, 16.5, "Backward")
    tank.turn_degrees(10, 10, True, 1)
    Claw.claw.reset()
    sleep(0.5)
    Claw.claw_open(120)
    sleep(0.5)
    tank.turn_degrees(10, -10, True, 1)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.distance_to_object(tank, 11, "Backward")
    tank.turn_degrees(10, -180, True, 1)
    init.debug_print("Finishing angle before check "+str(tank.gyro.angle))
    Navigation.gyro_check(tank, 5, -180)
    init.debug_print("Finishing angle after check "+str(tank.gyro.angle))
    Claw.claw_close(120)
    lift.on_for_rotations(20, 1)
    lift.reset()
    Navigation.gyro_check(tank, 5, -180)

    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))

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

def Innovate3(tank, lift, Claw):

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
    Claw.claw_close(100)
    sleep(0.5)
    lift.on_for_rotations(35, -0.9)
    #Navigation.distance_to_object(tank, 92, "Backward", 10)
    Navigation.new_move_incm(tank, -25, 92)

    #Do bridge mission
    tank.turn_degrees(10, 180, True, 1)
    Navigation.gyro_check(tank, 10, 180)
    #tank.turn_degrees(10, -100, True, 1)

    init.debug_print("The amount turned before check: " + str(tank.gyro.angle))
    Navigation.gyro_check(tank, 10, 180)
    Navigation.distance_to_object(tank, 28, "Forward", 15)

    tank.turn_degrees(10, -90, True, 1)
    Navigation.gyro_check(tank, 10, 90)
    #(Curr angle should be -90)
    Navigation.distance_to_object(tank, 12, "Forward", 15)


    tank.turn_degrees(10, -90, True, 1)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.distance_to_object(tank, 16.5, "Backward")
    tank.turn_degrees(10, 10, True, 1)
    Claw.claw.reset()
    sleep(0.5)
    Claw.claw_open(100)
    sleep(0.5)
    tank.turn_degrees(10, -10, True, 1)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.distance_to_object(tank, 11, "Backward")
    tank.turn_degrees(10, -90, True, 1)
    init.debug_print("Finishing angle before check "+str(tank.gyro.angle))
    Navigation.gyro_check(tank, 5, -90)
    init.debug_print("Finishing angle after check "+str(tank.gyro.angle))
    Claw.claw_close(120)
    '''lift.on_for_rotations(20, 1)'''
    lift.reset()

    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))

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

def Innovate4(tank, lift, Claw):

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
    Claw.claw_close(100)
    sleep(0.5)
    lift.on_for_rotations(35, -0.9)
    #Navigation.distance_to_object(tank, 92, "Backward", 10)
    Navigation.new_move_incm(tank, -25, 92)

    #Do bridge mission
    tank.turn_degrees(10, 180, True, 1)
    Navigation.gyro_check(tank, 10, 180)
    #tank.turn_degrees(10, -100, True, 1)

    init.debug_print("The amount turned before check: " + str(tank.gyro.angle))
    Navigation.gyro_check(tank, 10, 180)
    Navigation.distance_to_object(tank, 28, "Forward", 15)

    tank.turn_degrees(10, -90, True, 1)
    Navigation.gyro_check(tank, 10, 90)
    #(Curr angle should be -90)
    tank.on_for_rotations(15, 15, -1)
    Navigation.distance_to_object(tank, 33, "Forward", 15)


    tank.turn_degrees(10, -90, True, 1)
    return

    Navigation.gyro_check(tank, 5, 0)
    Navigation.distance_to_object(tank, 16.5, "Backward")
    tank.turn_degrees(10, 10, True, 1)
    Claw.claw.reset()
    sleep(0.5)
    Claw.claw_open(120)
    sleep(0.5)
    tank.turn_degrees(10, -10, True, 1)
    Navigation.gyro_check(tank, 5, 0)
    Navigation.distance_to_object(tank, 11, "Backward")
    tank.turn_degrees(10, -180, True, 1)
    init.debug_print("Finishing angle before check "+str(tank.gyro.angle))
    Navigation.gyro_check(tank, 5, -180)
    init.debug_print("Finishing angle after check "+str(tank.gyro.angle))
    Claw.claw_close(120)
    lift.on_for_rotations(20, 1)
    lift.reset()
    Navigation.gyro_check(tank, 5, -180)

    endtime = time.time()-start_time
    init.debug_print("TIME: "+str(endtime))

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



if __name__ == "__main__":
    #Innovate2(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw(
    Innovate3(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())
    #truck_3(Navigation.tank_init(), MediumMotor(OUTPUT_D), claw.Claw())

'''The code below is our old code, in case we need it:
Navigation.distance_to_object(tank, 50, "Backward") #Going forward from home. [This and the code below is all of the old code:]
    turn_left(20)
    turn_right(20)
    turn_left(tank, 20)
    turn_right(tank,0)
    Navigation.distance_to_object(tank, 18.5, "Forward")
    turn_right(tank, 91)
    #init.turn_to_angle(20, 90)
    #tank.on_for_rotations(-10, -10, 2.34)
    #tank.on_for_rotations(-10, -10, 2.12)
    #tank.on_for_rotations(10, 10, 1)
    Navigation.distance_to_object(tank, 49.5, "Backward") #Pushing trucks towards bridge.
    Navigation.distance_to_object(tank, 20, "Forward") #Backing out of truck configuration.
    time.sleep(1)
    #turn_right(64)
    #Navigation.distance_to_object(tank, 57, "Backward")
    #turn_right(70)
    #turn_right(30)
    #Navigation.distance_to_object(tank, 60, "Backward")
    init.debug_print("Total Time: " + str(time.time() - start_time))'''
