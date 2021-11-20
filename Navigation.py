#!/usr/bin/env python3

'''
Imports:
'''

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from time import sleep
from ev3dev2.sound import Sound
import init 

'''
Distance Goer 
'''
#Goes to certain distance        
def distance_to_object(tank, distance, direction):
 
    distance_not_reached = True

    #Number of wheel rotations needed to get there
    number_of_wheel_rotations = distance / 25.6353961

    rotationnumber = 0

    rotation = number_of_wheel_rotations / 10

    if rotation < 0.3:
        rotation = 0.2

    
    #The angle the robot started with
    inital_angle = tank.gyro.angle

    while number_of_wheel_rotations > 0:
        
        if (rotation > number_of_wheel_rotations):
            rotation = number_of_wheel_rotations

        if direction == "Forward":
            tank.on_for_rotations(10, 10, rotation, brake=False, block=True)
        if direction == "Backward":
            tank.on_for_rotations(-10, -10, rotation, brake=False, block=True)

          
        #Add rotation number
        rotationnumber += rotation
        number_of_wheel_rotations -= rotation

        #See's if robot veered of track, if so fixes it
        degrees_off = inital_angle - tank.gyro.angle

        if tank.gyro.angle < inital_angle: 
            tank.turn_right(20, abs(degrees_off))
        if tank.gyro.angle > inital_angle: 
            tank.turn_left(20, abs(degrees_off))

'''
Line Following Program:
'''
def Line_Following(tank, colorLeft, colorRight, distance):
    #Saying to use the global variables, and not def variables
    global speed 
    
    distance_not_reached = True

    #Current rotation 
    rotationnumber = 0

    #Number of wheel rotations needed to get there
    number_of_wheel_rotations = distance / 25.13

    while distance_not_reached == True:
        difference = colorLeft.reflected_light_intensity - colorRight.reflected_light_intensity

        tank.on_for_rotations(20, 20, rotation)

        if difference < 0: 
            #Left is closer to black, We have to turn left
            if difference > -4:
                tank.turn_right(20, 1)
            elif difference < -30:
                tank.turn_right(20, 4)
            elif difference < -20:
                tank.turn_right(20, 3)
            elif difference > - 10:
                tank.turn_right(20, 2)
                        

        if difference > 0:
            #Right is closer to black, we have to turn right
            if difference < 4:
                tank.turn_left(20, 1)
            elif difference > 30:
                tank.turn_left(20, 4)
            elif difference > 20:
                tank.turn_left(20, 3)
            elif difference < 10:
                tank.turn_left(20, 2)


        #Add rotation number
        rotationnumber += rotation

        #Checks if robot has reached destination
        if number_of_wheel_rotations < rotationnumber:
            #Stops the line following program
            distance_not_reached == False