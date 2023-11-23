# Horrible essai

Explication : ma version de [GRBL](https://github.com/vankesteren/grbl-servo) sur Arduino fonctionne mais la gestion du servo en 11 est défectueuse. Les servos SG90 et MG90S ne bougent pas du tout et le servo C577 tourne un tout petit peu (autour de 20 degrés au lieu e 180, comme si l'impulsion qui est censée déterminer l'angle du servomoteur était trop courte...).

Pourtant le PWM sur la sortie 11 varie avec les commandes M3 S255 ou M3 S10 (par exemple). 

Idée : coupler la sortie 11 de l'Arduino avec une entrée de raspberry pico ... sous Python pour gérer le moteur... Dans un premier temps je me contente d'allumer ou éteindre une LED. 

Sur Pico, le code est dans le dossier "surveille_PWM". 

Résultat : fonctionne.