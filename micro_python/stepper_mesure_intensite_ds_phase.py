"""Mesure de l'intensité dans une bobine du stepper 28BYJ-48"""


from stepmotor import Stepmotor
import time

myStepMotor = Stepmotor(21, 20, 19, 18)

speed = 4000 * 1
sleep= 0.00
n = 0
while True:
    # Il semble que ce moteur soit très lent. Le denier paramètre
    # ne doit pas être inférieur à 2000. 
        myStepMotor.moveSteps(1, 100 , speed)
        myStepMotor.stop()
        time.sleep(sleep)
        
        myStepMotor.moveSteps(0, 100 , speed)
        myStepMotor.stop()
        time.sleep(sleep)
        print(f"Fin du cycle {n}")
        n =+1

print("Erreur non prévue avec le Moteur")

myStepMotor.stop()