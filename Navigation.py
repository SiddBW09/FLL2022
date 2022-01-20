#!/usr/bin/env python3

'''
Imports:
'''

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from ev3dev2.motor import MediumMotor
from time import sleep
from ev3dev2.sound import Sound
import init

def tank_init():
    my_tank = MoveTank(OUTPUT_A, OUTPUT_B)

     # Init Color Sensors
    #colorRight = ColorSensor(INPUT_2)
    #colorLeft = ColorSensor(INPUT_3)

    # init Gyro Sensor
    my_tank.gyro = GyroSensor(INPUT_1)
    my_tank.gyro.mode='GYRO-ANG'
    my_tank.gyro.reset()
    return my_tank

'''
Distance Goer
'''
#Goes to certain distance
def distance_to_object(tank, distance, direction, speed=10):

    distance_not_reached = True

    #Number of wheel rotations needed to get there
    number_of_wheel_rotations = distance / 25.6353961

    rotation = number_of_wheel_rotations / 10

    if rotation < 0.3:
        rotation = 0.2

    sleep(0.5)
    #The angle the robot started with
    inital_angle = tank.gyro.angle

    while number_of_wheel_rotations > 0:

        if (rotation > number_of_wheel_rotations):
            rotation = number_of_wheel_rotations

        if direction == "Forward":
            tank.on_for_rotations(speed, speed, rotation, brake=False, block=True)
        if direction == "Backward":
            tank.on_for_rotations(-speed, -speed, rotation, brake=False, block=True)


        #Minus current rotation from total rotations needed
        number_of_wheel_rotations -= rotation

        #See's if robot veered of track, if so fixes it
        degrees_off = inital_angle - tank.gyro.angle

        tank.turn_degrees(10, degrees_off)
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

def turn_degrees(tank, degrees, direction, speed):
    initial_ang = tank.gyro.angle


    if direction == "Right":
        target_ang = initial_ang + degrees
        tank.turn_right(speed, degrees)

        sleep(0.5)

        if target_ang != tank.gyro.angle:
            target_ang -= tank.gyro.angle

            tank.turn_degrees(5, target_ang)
            sleep(0.5)

    if direction == "Left":
        target_ang = initial_ang - degrees

        tank.turn_left(speed, degrees)

        sleep(0.5)

        if target_ang != tank.gyro.angle:
            target_ang -= tank.gyro.angle

            tank.turn_degrees(5, target_ang)
            sleep(0.5)

def gyro_check (tank, speed, angle):
    angle_now = tank.gyro.angle
    if angle_now > angle:
        #Turn angle-90 to the left
        offset1 = angle_now-angle
        if (offset1 > 1):
            tank.turn_degrees(speed, -1*(offset1), True, .25)
            init.debug_print("Final angle turned: " + str(tank.gyro.angle))
    elif angle_now < angle:
        #Turn 90-angle to the right
        offset1 = angle-angle_now
        if (offset1 > 1):
            tank.turn_degrees(speed, offset1, True, .25)
            init.debug_print("Final angle turned: " + str(tank.gyro.angle))


    while tank.gyro.angle != angle:
        tank.turn_degrees(5, angle-tank.gyro.angle, True, 0.1)


def new_move_incm(tank, speed, distance):

    #Number of wheel rotations needed to get there
    number_of_wheel_rotations = distance / 25.6353961
    tank.on_for_rotations(speed, speed, distance / 25.6353961)

def follow_forever(tank, cm, lm):

    rotations_needed = cm/0.0712094336
    motorPos=lm.position
    if (motorPos<0):
        motorPos = motorPos*-1
    if (motorPos >= rotations_needed):
        return False

    return True


def distance_goer(tank, distance, speed, angle):
    tank.reset()
    left_motor = LargeMotor(OUTPUT_A)
    left_motor.reset()
    tank.follow_gyro_angle(
        kp=11.3, ki=0.05, kd=3.2,
        speed=SpeedPercent(speed),
        target_angle=angle,
        sleep_time=0.01,
        follow_for=follow_forever,
        cm=distance, lm=left_motor)

    gyro_check(tank, 5, angle)



