# Surveiller un signal PWM généré par un Arduino.

# Le signal PWM sera stabilité par un condensateur.
import time
from machine import Pin

# Entrée:
entree = Pin(13, Pin.IN, Pin.PULL_DOWN) 


# Sortie
led=Pin(15,Pin.OUT)
#create LED object from Pin 25,Set Pin 25 to output

while True:
    if entree.value() == 1:
        #Set led turn on   
        led.value(1)
        print("On")
    else:        
        #Set led turn off
        led.value(0)
        print("Off")
    time.sleep(0.05)