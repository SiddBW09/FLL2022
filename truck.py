#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B,MoveTank, SpeedPercent, follow_for_ms, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import Navigation
import init
from time import sleep
from ev3dev2.motor import MediumMotor

def code():
    #Initializing tank
    tank = MoveTank(OUTPUT_D, OUTPUT_A)
    tank.gyro = GyroSensor(INPUT_1)
    tank.gyro.mode='GYRO-ANG'
    tank.gyro.calibrate()
    tank.gyro = GyroSensor(INPUT_1)

    def turn_right(angle): #Function which accurately turns the robot 90 degrees to the right.
        tank.turn_right(10, angle-20)
        gyroangle = tank.gyro.angle
        offset = (angle - gyroangle)

        #Printing values to check the angles.
        sleep(1)
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

    def turn_left(angle): #Functions which accurately turns the robot 90 degrees to the right.
            tank.gyro.reset()
            tank.turn_left(10, angle-20)
            gyroangle = tank.gyro.angle
            offset = (angle - gyroangle)

            #Printing values to check the angles.
            sleep(1)
            init.debug_print("Amount of degrees turned: " + str(gyroangle))
            init.debug_print("The offset is: " + str(offset))

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

    #Execute the sequence to complete the missions.
    #tank.on_for_rotations(-10, -10, 1)
    #tank.on_for_rotations(-10, -10, 1.45)

    tank.gyro.reset()
    #tank.on_for_rotations(-10, -10, 1.48)
    #tank.on_for_rotations(-10, -10, 1.55)
    Navigation.distance_to_object(tank, 50, "Backward") #Going forward from home.
    '''turn_left(20)
    turn_right(20)'''
    turn_left(20)
    turn_right(0)
    Navigation.distance_to_object(tank, 18.2, "Forward")
    turn_right(90)
    #init.turn_to_angle(20, 90)
    #tank.on_for_rotations(-10, -10, 2.34)
    #tank.on_for_rotations(-10, -10, 2.12)
    #tank.on_for_rotations(10, 10, 1)
    Navigation.distance_to_object(tank, 49, "Backward") #Pushing trucks towards bridge.
    Navigation.distance_to_object(tank, 45, "Forward") #Backing out of truck configuration.
    init.debug_print ("At the end of the code the angle is: " + str(tank.gyro.angle))

if __name__ == "__main__":
    code()
