// v1
// Pour raccorder 2 V-slots
// arrondir les angles
// Enlever 1 mm sur les bords pour éviter les frottements.
// Montage pour axe Z.

include <./MCAD/boxes.scad>
// exemple !
// roundedBox([20, 30, 40], 2, true);
A_x = 40;
B_y = 40;

edge = 0 ; // enlever cette valeur des bords.
epp = 8 ;

dia = 5 ;  // diameter of holes
eps = 0.01 ; 

contre_trou_hauteur = 3; 

module connector(A, B){
    difference() {
    // cube([A_x, B_y, epp]);
        translate([A/2, B/2, epp/2])
    roundedBox([A - (2* edge), B -(2 * edge), epp], 2, true, $fn=20);
    {
        // holes on X axis
        for (i = [ 0 : 2 ]) {
          translate([10 +  i*20, 10, 0-eps]){
            cylinder(r=dia/2, h=10 + 2*eps, $fn = 30);
            cylinder(r=5, h=3 + 2*eps, $fn = 30);
              };
          };

        for (j = [ 0 : 2 ]) {
          translate([10 +  j*20, 30, 0-eps])
            cylinder(r=dia/2, h=10 + 2*eps, $fn = 30);
           
          translate([10 +  j*20, 30, epp - contre_trou_hauteur + eps])
           cylinder(r=5, h=contre_trou_hauteur + 2*eps, $fn = 30); 
          };
          
    }
    }
}

module narrow_connector(){
    connector(A_x, B_y); 
};

narrow_connector(); 


// connector();

