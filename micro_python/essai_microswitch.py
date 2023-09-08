from machine import	Pin
from stepmotor import Stepmotor
import time

myStepMotor = Stepmotor(21, 20, 19, 18)


# si pas de pull_DOWN, on obtient un signal erratique. 
button = Pin(12, Pin.IN, Pin.PULL_DOWN)
n = 0
speed = 4000

step = 1 * 16
pressed = False

def move(dir, step=step):
    print("step", step)
    if not pressed :
        myStepMotor.moveSteps(dir, step  , speed)
        # myStepMotor.stop()
        # time.sleep(0.05)
    else:
        print("Stop")

def to_right( **kwargs):
    move(0, **kwargs)
    
def to_left(**kwargs):
    move(1, **kwargs)
    
def to_left_until_swith_is_pressed():
    encore = True
    pressed = False
    
    while encore:
        myStepMotor.moveSteps(1, 20  , speed)
        but = button.value()
        time.sleep(0.001)
        if but == 1: # debounce
            time.sleep(0.010)
            but2 = button.value()
            if but2 ==1:
                print("Pressed")
                encore = False
        
            
        
        
        


# A switch (NO : normaly opened) is connected : one pin is connected to 3.3V,
# the other pin is connected to GP12. No resistance, so
# use an internal pull_resistance.
while True:
    but = button.value()
    time.sleep(0.001)
    if but == 1: # debounce
        time.sleep(0.010)
        but2 = button.value()
        if but2 ==1:
            print("Pressed")
            pressed = True

    # Il semble que ce moteur soit très lent. Le denier paramètre
    # ne doit pas être inférieur à 2000. 
    to_right()
    to_left()

    time.sleep(0.2)
    n += 1
    print(f"Fin du cycle {n}")

        