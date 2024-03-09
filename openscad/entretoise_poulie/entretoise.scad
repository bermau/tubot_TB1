
epaisseur_poulie = 8.5  ;
dia_ext= 7; 
dia_int = 5.4;

hauteur = 20 / 2 - epaisseur_poulie / 2 ;
hauteur = 2 ; 
$fn= 60;
module entretoise(){
        difference(){
        cylinder(h= hauteur, r = dia_ext/2);
    cylinder(h= hauteur, r = dia_int/2);
    
        }
};




entretoise();