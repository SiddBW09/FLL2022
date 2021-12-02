#!/usr/bin/env python3
import ev3dev.ev3
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, MoveTank, SpeedPercent, follow_for_ms, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import Navigation
import time
from ev3dev2.motor import OUTPUT_B, MediumMotor
import init
import claw

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
    # Init Color Sensors

    truck_to_bridge(tank, lift)
    return

    colorRight = ColorSensor(INPUT_2)
    colorLeft = ColorSensor(INPUT_3)
    start_time = time.time()

    #turn_right(tank, 45)
    Navigation.turn_degrees(tank, 45, "Right")
    Navigation.distance_to_object(tank, 41.595, "Backward")
    Navigation.turn_degrees(tank, 45, "Right")
    angle_now = tank.gyro.angle
    init.debug_print("Angle (after 1 offset check): " + str(angle_now))
    if angle_now > 90:
        #Turn angle-90 to the left
        offset1 = int(angle_now-90)
        Navigation.turn_degrees(tank, int(offset1), "Left")
        init.debug_print("Final angle turned: " + str(angle_now - offset1))
    elif angle_now < 90:
        #Turn 90-angle to the right
        offset2 = int(90-angle_now)
        Navigation.turn_degrees(tank, int(offset2), "Right")
        init.debug_print("Final angle turned: " + str(angle_now - offset2))
    Navigation.distance_to_object(tank, 22, "Backward") #Push trucks together.
    Navigation.distance_to_object(tank, 17, "Forward") #Back up from trucks.
    Navigation.turn_degrees(tank, 45, "Left")
    angle_now = tank.gyro.angle
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
        init.debug_print("Final angle turned: " + str(angle_now - offset2))
    Navigation.distance_to_object(tank, 20, "Backward")
    lift.on_for_rotations(-20, 1)

    Navigation.turn_degrees(tank, 45, "Right") #Parallel to trucks.
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
    return
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
    tank.on_for_rotations(10, 10, 0.55)
    tank.turn_degrees(20, -35, True, 1)

    init.debug_print(tank.gyro.angle)
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

if __name__ == "__main__":
    truck_2()

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
