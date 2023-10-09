"""Premier test du 28BYJ-48"""

print("Salut toi !")

from stepmotor import Stepmotor
import time

myStepMotor = Stepmotor(21, 20, 19, 18)

speed = 4000 * 10000


while True:
    # Il semble que ce moteur soit très lent. Le denier paramètre
    # ne doit pas être inférieur à 2000. 
        myStepMotor.moveSteps(1, 8 * 64 , 4000)
        # myStepMotor.stop()
        time.sleep(0.2)
        
        myStepMotor.moveSteps(0, 8 * 64 , 4000)
        # myStepMotor.stop()
        time.sleep(0.2)
        n += 1
        print(f"Fin du cycle {n}")

print("Erreur non prévue avec le Moteur")

myStepMotor.stop()