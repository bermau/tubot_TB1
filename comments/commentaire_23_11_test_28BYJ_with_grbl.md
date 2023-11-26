# 23_11_test_28BYJ_with_grbl

Le but est de tester un stepper 28BYJ_sur le grbl.

La version de grbl utilisée est celle de (https://github.com/vankesteren/grbl-servo). 

Pour cette branche, j'ai mis un moment à comprendre qu'il fallait "régler" les paramètres du SG90. 

spindle_control.c : is OK for a SG90 with :  
``` c
#define RC_SERVO_SHORT      15      //initial  7; puis 11 ; set min pulse duration to (7 = 0.5ms, 15 = 1.03ms, 20=1.40ms)    // RC Servo
#define RC_SERVO_LONG       38      //initial  17 ; puis 30 ; set max pulse duration (38 = 2.49ms, 31 = 2.05ms)                // RC Servo
```

En pratique, par la suite, je suis passé à la version de grbl de https://github.com/ArcaEge/grbl-28byj-48-pen-plotter-servo 