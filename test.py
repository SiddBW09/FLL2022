#!/usr/bin/env python3

'''
Imports:
'''
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B,MoveTank, SpeedPercent, follow_for_ms, MoveSteering, follow_for_forever
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import Navigation
from time import sleep
import time
from ev3dev2.motor import OUTPUT_B, MediumMotor
import Navigation
import init
import claw


timercnt = 0

def follow_forever(tank, distance, pranav):
    init.debug_print(lm.position)
    init.debug_print(pranav)
    if (lm.position > distance):
        return False
    init.debug_print(lm.count_per_rot)
    return True

tank = init.init_and_create_movetank()
lm = LargeMotor(OUTPUT_A)
#tank.on(10,10)
init.debug_print(tank.gyro.angle)
tank.follow_gyro_angle(
        kp=11.3, ki=0.05, kd=3.2,
        speed=SpeedPercent(50),
        target_angle=0,
        sleep_time=0.01,
        follow_for=follow_forever,
        distance=1500, pranav="awesome")
i = 0
while True:
    i=i+1
    init.debug_print(lm.position)
    init.debug_print(lm.count_per_rot)
    sleep(0.5)
    if (i > 20):
        break

tank.stop()

'''
tank = MoveTank(OUTPUT_A, OUTPUT_B)
claw = claw.Claw()
lift = MediumMotor(OUTPUT_D)

lift.on_for_rotations(10, 1.5)

if claw.claw_close_5() == 'blocked':
    init.debug_print("Doin Something About it")
elif claw.claw_close_5():

    lift.on_for_rotations(10, -2)
else:
    tank.on_for_rotations(10, 5, -2)
'''
