#!/usr/bin/env python3

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from ev3dev2.motor import MediumMotor
from time import sleep, time
from ev3dev2.sound import Sound
import Navigation
import init

# test
#tank = Navigation.tank_init()


def gyro_check(tank, speed, angle):
    angle_now = tank.gyro.angle
    #init.debug_print("cuur angle: " + str(tank.gyro.angle))
    if angle_now > angle:
        # Turn angle-90 to the left
        offset1 = angle_now-angle
        # if (offset1 > 1):
        tank.turn_degrees(speed, -1*(offset1), True, .1)
        #init.debug_print("Final angle turned: " + str(tank.gyro.angle))
    elif angle_now < angle:
        # Turn 90-angle to the right
        offset1 = angle-angle_now
        # if (offset1 > 1):
        tank.turn_degrees(speed, offset1, True, .1)
        #init.debug_print("Final angle turned: " + str(tank.gyro.angle))


def goToMission(tank, fork):
    tank.on_for_rotations(15, 15, 1)
    sleep(0.5)
    tank.on_for_rotations(20, 3, 0.4)  # turning right, L speed, R speed
    sleep(0.5)
    tank.on_for_rotations(-15, -15, 0.7)
    sleep(0.5)
    tank.on_for_rotations(3, 20, 0.7)  # turn parallel to hydrodam

def InnovMission(tank, fork):
    goToMission2(tank, fork)
    operateMission(tank, fork)



def goToMission2(tank, fork):
    tank.gyro.reset()
    Navigation.distance_goer(tank, 37, 25, 0)
    fork.on_for_rotations(-20, 0.2)
    Navigation.gyro_check(tank, 5, 45)
    #Navigation.distance_goer(tank, 78, 10, 45)
    Navigation.distance_goer(tank, 5, 25, 45)
    fork.on_for_rotations(20, 0.2)
    Navigation.distance_goer(tank, 42, 25, 45)
    Navigation.gyro_check(tank, 5, 90)
    Navigation.distance_goer(tank, 10, -25, 90)

def operateMission(tank, fork):
    tank.gyro.reset()
    fork.reset()
    #Navigation.distance_goer(tank, 6, -5, 0) #OG distance was 6
    Navigation.distance_goer(tank, 6.45, -5, 0)
    fork.on_for_rotations(-60, 0.15)  #lift big bar
    #fork.on_for_rotations(5, 0.08)
    sleep(0.3)
    #OG val 5, -10
    Navigation.goer_no_gyro(tank, 8, -10)
    Navigation.goer_no_gyro(tank, 1, 5)
    #tank.on_for_rotations(-10, -10, 0.16, brake=True, block=True)
    sleep(0.3)
    #OG vaal 0.18
    #NEW CODE TO TEST
    #Navigation.gyro_check(tank, 10, 3)
    fork.on_for_rotations(10, 0.18) #put thing down
    Navigation.distance_goer(tank, 40.45, 35, -5) #OG dist 40

    Navigation.gyro_check(tank, 10, 15)
    return
    Navigation.distance_goer(tank, 10, 20, 0)
    Navigation.distance_goer(tank, 40, 20, -10)


def pushdownThingy(tank, fork):
    tank.gyro.reset()
    fork.reset()
    #fork.on_for_rotations(-60, 0.2)
        #tank.turn_degrees(5, 90, True, 0.05)
    #home_to_plant_backwards(tank, fork)
    #sleep(1)
    #fork.on_for_rotations(10, 0.45)
    fork.reset()
    #fork.on_for_rotations(-5, 0.1)
    Navigation.distance_goer(tank, 9.5, -5, 90) #forward to mission build (tank, distance, speed, angle)
    #Navigation.gyro_check(tank, 5, 0)
    #tank.on_for_rotations(-10, -10, 0.13, brake=True,
                          #block=True)  # forward to mission

    fork.on_for_rotations(-60, 0.3)  # lift big bar
    fork.on_for_rotations(5, 0.08)
    #return
    #Navigation.gyro_check(tank, 5, 0)
    #forward 5 go back 3
    tank.on_for_rotations(-5, -5, 0.3, brake=True, block=True)
    sleep(0.5)
    #tank.on_for_rotations(5, 5, 0.3)
    fork.on_for_rotations(10, 0.27)  # hit smaller bar
    fork.on_for_rotations(-10, 0.2)
    sleep(0.3)
    # go back to meet innovation piece
    tank.on_for_rotations(10, 10, 0.17, brake=True, block=True)
    sleep(0.3)
    fork.on_for_rotations(10, 0.23)  # grip down on innovation piece
    Navigation.distance_goer(tank, 30, 20, -10)
    #tank.on_for_rotations(30, 30, 1.8, brake=True,
    #                      block=True)  # Back to hydrogen plant

def home_to_plant(tank, fork):
    Navigation.distance_goer(tank, 45, -30, 0)
    Navigation.gyro_check (tank, 15, 25)
    Navigation.distance_goer(tank, 50, -25, 25)
    Navigation.gyro_check (tank, 15, -35)
    Navigation.distance_goer(tank, 5, 30, -35)

def home_to_plant_backwards(tank, fork):
    fork.on_for_rotations(5, 0.05)
    originalAngle = tank.gyro.angle
    Navigation.distance_goer(tank, 42, 25, 0) #going left towards toy factory
    #Navigation.gyro_check (tank, 15, 45)
    turnDegree = 45-originalAngle
    tank.turn_degrees(10, turnDegree, True, 0.05)
    sleep(0.5)
    #Navigation.distance_goer(tank, 5, 20, 30)
    #tank.turn_degrees(10, 15, True, 0.05)
    Navigation.distance_goer(tank, 30, 25, 45) #backwards towards innovation circle area
    sleep(0.5)
    #Navigation.gyro_check (tank, 10, 90)
    originalAngle = tank.gyro.angle
    init.debug_print(originalAngle)
    turnDegree = 90-originalAngle
    init.debug_print(turnDegree)
    tank.turn_degrees(5, turnDegree, True, 0.05)
    init.debug_print(tank.gyro.angle)
    #Navigation.distance_goer(tank, 50, -25, 25)
    #Navigation.gyro_check (tank, 15, -35)
    #Navigation.distance_goer(tank, 5, 30, -35)
#goToMission(tank, fork)

if __name__ == "__main__":
    tank = MoveTank(OUTPUT_A, OUTPUT_B)
    fork = LargeMotor(OUTPUT_C)
    tank.gyro = GyroSensor(INPUT_1)
    time1 = time()
    tank.gyro.reset()
    goToMission2(tank, fork)
    operateMission(tank,fork)

    #pushdownThingy(tank, fork)
    time2 = time()
    init.debug_print(time2-time1)



# ON_FOR_ROTATIONS PARAMETERS: speed (+ goes backward), speed, rotations, brake=True, block=True
