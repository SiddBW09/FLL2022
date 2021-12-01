from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from ev3dev2.motor import MediumMotor
from time import sleep
from ev3dev2.sound import Sound
import init

class Claw():
    def __init__(self):
        self.claw = MediumMotor(OUTPUT_C)

    def claw_open(self, percent):
        self.claw.reset()
        self.claw.on_for_rotations(-30, 0.1)

    def claw_close(self, percent):
        i = 0
        self.claw.reset()
        while True:

            self.claw.on_for_rotations(10, 0.01, brake = False)

            if 'stalled' in self.claw.state:
                init.debug_print(self.claw.state)
                break

            i += 1
        init.debug_print(i)

        if i >= 10:
            print("Did not catch brick")
            return False

        else:
            return True

        return


