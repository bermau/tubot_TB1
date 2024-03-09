
epaisseur_poulie = 8.5  ;
dia_ext= 7; 
dia_int = 5.4;
eps = 0.01; 

hauteur = 20 / 2 - epaisseur_poulie / 2 ;
$fn= 60;

module entretoise(){
        difference(){
        cylinder(h= hauteur , r2 = dia_ext/2, r1=(dia_ext+4)/2);
        translate([0, 0, -eps/2]) 
        cylinder(h= hauteur+eps, r = dia_int/2);
    
        }
};


entretoise();