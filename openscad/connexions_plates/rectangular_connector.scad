// v1
// Pour raccorder 2 V-slots
// arrondir les angles
// Enlever 1 mm sur les bords pour éviter les frottements. 

include <./MCAD/boxes.scad>
// exemple !
// roundedBox([20, 30, 40], 2, true);
A_x = 40;
B_x = 40;

edge = 1 ; // enlever cette valeur des bords.

A_y = A_x;
B_y=  B_x;

epp = 4 ;

dia = 5 ;  // diameter of holes
eps = 0.01 ; 


module connector(){
    difference() {
    // cube([A_x, B_y, epp]);
        translate([A_x/2, B_y/2, epp/2])
    roundedBox([A_x - (2* edge), B_y -(2 * edge), epp], 2, true, $fn=20);
    {
        // holes on X axis
        for (i = [ 0 : 2 ]) {
          translate([10 +  i*20, 10, 0-eps])
            cylinder(r=dia/2, h=10 + 2*eps, $fn = 30);         
          };
        for (j = [ 0 : 2 ]) {
          translate([10 +  j*20, 30, 0-eps])
            cylinder(r=dia/2, h=10 + 2*eps, $fn = 30);         
          };
 
    }
    }
}


connector();

