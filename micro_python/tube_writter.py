from machine import Pin
from stepmotor import Stepmotor
import time


class MonStepper(object):
    def __init__(self):
        print("Debut Init")
        self.myStepMotor = Stepmotor(21, 20, 19, 18)

        # si pas de pull_DOWN, on obtient un signal erratique.
        self.button = Pin(12, Pin.IN, Pin.PULL_DOWN)

        self.speed = 2500

        self.step = 4 * 64
        self.pressed = False
        print("Fin de Init")

    def move(self, dir, step=None):
        if step is None:
            step = self.step
        print("step", self.step)
        if not self.pressed:
            self.myStepMotor.moveSteps(dir, step, self.speed)
        else:
            print("Stop")

    def to_right(self, **kwargs):
        self.move(0, **kwargs)

    def to_left(self, **kwargs):
        self.move(1, **kwargs)

    def to_left_until_swith_is_pressed(self):
        encore = True
        self.pressed = False

        while encore:
            self.myStepMotor.moveSteps(1, 20, speed)
            but = button.value()
            time.sleep(0.001)
            if but == 1:  # debounce
                time.sleep(0.010)
                but2 = self.button.value()
                if but2 == 1:
                    print("Pressed")
                    encore = False


# A switch (NO : normaly opened) is connected : one pin is connected to 3.3V,
# the other pin is connected to GP12. No resistance, so
# use an internal pull_resistance.
# if __name__ == '__main__':

print("STRATING")

X = MonStepper()
n = 0

while True:
    but = X.button.value()
    time.sleep(0.001)
    if but == 1:  # debounce
        time.sleep(0.010)
        but2 = X.button.value()
        if but2 == 1:
            print("Pressed")
            X.pressed = True

    # Il semble que ce moteur soit très lent. Le dernier paramètre
    # ne doit pas être inférieur à 2000. 
    X.to_right()
    X.to_left()

    time.sleep(0.2)
    n += 1
    print(f"Fin du cycle {n}")
