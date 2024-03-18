# test du servo en 16 (position logique)

from servo import Servo

import time

class BM_servo:
    def __init__(self, pin):
        self.servo = Servo(pin)
        
    def test(self):
        print("test simple du servo")
        self.servo.ServoAngle(0)
        time.sleep(1)
        self. servo.ServoAngle(180)
        time.sleep(1)
        self.servo.ServoAngle(0)
        for j in range(4):
            
                for i in range(0, 180, 1):
                    self.servo.ServoAngle(i)
                    time.sleep_ms(15)
                for i in range(180, 0, -1):
                    self.servo.ServoAngle(i)
#                     time.sleep_ms(15)
#             except:
#                 self. servo.deinit()
#                 print("servo problem during short test")
    
    def long_test(self):
        for truc in range(3):
            print(f"test : {truc}")
            try:
                self.servo.ServoAngle(0)
                time.sleep_ms(500)
                self.servo.ServoAngle(180)
                time.sleep_ms(1000)
            except:
                self. servo.deinit()
                print("servo problem during long test")
    
    def test_pen(self):
        for i in range(10):
            self.pen_up()
            time.sleep(0.5)
            self.pen_down()
            time.sleep(0.3)        
    
    def pen_up(self):
        print('up')
        self.servo.ServoAngle(35)
        time.sleep_ms(50)
        
    def pen_down(self):
        print('down')
        self.servo.ServoAngle(25)
        time.sleep_ms(50)   

Y = BM_servo(16) # position logique
for i in range(2):
    #Y.test_pen()
    # Y.test()   
    Y.long_test()