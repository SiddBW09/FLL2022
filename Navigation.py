#!/usr/bin/env python3

'''
Imports:
'''

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from ev3dev2.motor import MediumMotor
from time import sleep, time
from ev3dev2.sound import Sound
import main, init

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

def gyro_check (tank, speed, angle):
    angle_now = tank.gyro.angle
    #init.debug_print("cuur angle: " + str(tank.gyro.angle))
    if angle_now > angle:
        #Turn angle-90 to the left
        offset1 = angle_now-angle
        #if (offset1 > 1):
        tank.turn_degrees(speed, -1*(offset1), True, .1)
        #init.debug_print("Final angle turned: " + str(tank.gyro.angle))
    elif angle_now < angle:
        #Turn 90-angle to the right
        offset1 = angle-angle_now
        #if (offset1 > 1):
        tank.turn_degrees(speed, offset1, True, .1)
        #init.debug_print("Final angle turned: " + str(tank.gyro.angle))


    # while tank.gyro.angle != angle:
    #     tank.turn_degrees(5, angle-tank.gyro.angle, True, 0.25)

def goer_no_gyro(tank, cm, speed):
    rotations_needed = cm/26

    tank.on_for_rotations(speed, speed, rotations_needed)

def follow_forever(tank, cm, lm, startTime):


    rotations_needed = cm/0.0712094336
    motorPos=lm.position

    if (motorPos<0):
        motorPos = motorPos*-1
    if (motorPos >= rotations_needed):
        return False


    if time()-startTime > 2:
        init.debug_print("Exception")
        raise NameError("STOP")



    return True


def distance_goer(tank, distance, speed, angle):
    tank.reset()
    left_motor = LargeMotor(OUTPUT_A)
    left_motor.reset()
    sleep = 0.02

    if abs(speed) >= 30:
        sleep = 0.005



    tank.follow_gyro_angle(
        kp=11.3, ki=0.05, kd=3.2,
        speed=SpeedPercent(speed),
        target_angle=angle,
        sleep_time=sleep,
        follow_for=follow_forever,
        cm=distance, lm=left_motor, startTime=time())

    gyro_check(tank, 5, angle)





