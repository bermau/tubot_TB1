from machine import Pin

from stepmotor import Stepmotor
from servo import Servo

import time


# pins :
# IO/12 : switch for X
# IO/ 18n 19n, 20, 21 : stepper X
# test du servo pour axe Z (lever baisse l'outils crayon) en 14

class BM_servo:
    def __init__(self, pin):
        self.servo = Servo(pin)
        
    def test(self):
        print("entrée dans test")
        self.servo.ServoAngle(0)
        time.sleep(1)
        self. servo.ServoAngle(180)
        time.sleep(1)
        self.servo.ServoAngle(0)
        for j in range(3):
            try:
                for i in range(0, 180, 1):
                    self.servo.ServoAngle(i)
                    time.sleep_ms(15)
                for i in range(180, 0, -1):
                    self.servo.ServoAngle(i)
                    time.sleep_ms(15)
            except:
                self. servo.deinit()
                print("servo progblem during short test")
    
    def long_test(self):
        for truc in range(3):
            print(f"test {truc}")
            try:
                self.servo.ServoAngle(0)
                time.sleep_ms(500)
                self.servo.ServoAngle(180)
                time.sleep_ms(1000)
            except:
                self. servo.deinit()
                print("servo problem during long test")
        


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
    
    def stop(self):
        self.myStepMotor.stop()
    

    def to_right(self, **kwargs):
        self.move(0, **kwargs)
        self.stop()

    def to_left(self, **kwargs):
        self.move(1, **kwargs)
        self.stop()
        
    def to_left_until_swith_is_pressed(self):
        encore = True
        self.pressed = False

        while encore:
            self.myStepMotor.moveSteps(1, 20, self.speed)
            but = button.value()
            time.sleep(0.001)
            if but == 1:  # debounce
                time.sleep(0.010)
                but2 = self.button.value()
                if but2 == 1:
                    print("Pressed")
                    encore = False
    def test(self):
        for n in range(3):
            print("Boucle sur X")
            but = self.button.value()
            time.sleep(0.001)
            if but == 1:  # debounce
                time.sleep(0.010)
                but2 = self.button.value()
                if but2 == 1:
                    print("Pressed")
                    self.pressed = True

            # Il semble que ce moteur soit très lent. Le dernier paramètre
            # ne doit pas être inférieur à 2000. 
            self.to_right()
            self.to_left()

            time.sleep(0.2)
            self.myStepMotor.stop()	

            print(f"Fin du cycle {n}")
        

# A switch (NO : normaly opened) is connected : one pin is connected to 3.3V,
# the other pin is connected to GP12. No resistance, so
# use an internal pull_resistance.
# if __name__ == '__main__':

print("STRATING")

X = MonStepper()

pen = BM_servo(16)
rot = BM_servo(17)

time.sleep(1)
# 
# Y.servo.ServoAngle(0)
# time.sleep(0.5)
# Y.servo.ServoAngle(30)
# Y.servo.ServoAngle(0)
# time.sleep(0.5)
# Y.servo.ServoAngle(30)
# Y.servo.ServoAngle(0)
# time.sleep(0.5)
# Y.servo.ServoAngle(30)

print("Moteurs initialisés")
for i in range(10):
    print ("test", i)
    print("test rotation")
    rot.test()
    print("Lancement des tests sur pen")
    pen.long_test()
    print("Lancement des tests sur axe_ X")
    X.test()
print("OK !")
 