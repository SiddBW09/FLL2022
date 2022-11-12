#!/usr/bin/env python3

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from ev3dev2.motor import MediumMotor
from time import sleep
from ev3dev2.sound import Sound
import Navigation

#test
#tank = Navigation.tank_init()
tank = MoveTank(OUTPUT_A, OUTPUT_B)
fork=LargeMotor(OUTPUT_C)
tank.gyro = GyroSensor(INPUT_1)

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

def goToMission (tank, fork):
    tank.on_for_rotations(15, 15, 1)
    sleep(0.5)
    tank.on_for_rotations(20, 3, 0.4) #turning right, L speed, R speed
    sleep(0.5)
    tank.on_for_rotations(-15, -15, 0.7)
    sleep(0.5)
    tank.on_for_rotations(3, 20, 0.7) #turn parallel to hydrodam


def pushdownThingy (tank, fork):
    tank.gyro.reset()
    fork.on_for_rotations(10, 0.47)
    sleep(0.5)
    Navigation.gyro_check(tank, 5, 0)
    tank.on_for_rotations(-10, -10, 0.155, brake=True, block=True) #forward to mission
    fork.on_for_rotations(-50, 0.3) #lift big bar
    Navigation.gyro_check(tank, 5, 0)
    tank.on_for_rotations(-5, -5, 0.35, brake=True, block=True)
    sleep(0.5)
    tank.on_for_rotations(5, 5, 0.2)
    fork.on_for_rotations(10, 0.27) #hit smaller bar
    fork.on_for_rotations(-10, 0.2)
    sleep(0.3)
    tank.on_for_rotations(10, 10, 0.15, brake=True, block=True) #go back to meet innovation piece
    sleep(0.3)
    fork.on_for_rotations(10, 0.23) #grip down on innovation piece
    tank.on_for_rotations(30, 30, 1.8, brake=True, block=True) #Back to hydrogen plant

#goToMission(tank, fork)
pushdownThingy(tank, fork)


#ON_FOR_ROTATIONS PARAMETERS: speed (+ goes backward), speed, rotations, brake=True, block=True
