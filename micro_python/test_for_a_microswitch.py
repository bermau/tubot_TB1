from machine import	Pin

import time

# si pas de pull_DOWN, on obtient un signal erratique. 
button = Pin(12, Pin.IN, Pin.PULL_DOWN)
i = 0

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
    else:
        print('no pressed')

        
#         if button.value() == 0:
#             print(i, "pas pressé")
#         else:
#             print(i, "pressé")
#         i +=1    
# except:
#    pass