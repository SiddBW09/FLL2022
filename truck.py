from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B,MoveTank, SpeedPercent, follow_for_ms, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import Navigation
from ev3dev2.motor import MediumMotor

def code():
    tank = MoveTank(OUTPUT_D, OUTPUT_A)
    tank.gyro = GyroSensor(INPUT_1)
    tank.gyro.mode='GYRO-ANG'
    tank.gyro.calibrate()

    tank.on_for_rotations(10, 10, 1)

#Execute
if __name__ == "__main__":
    code()
