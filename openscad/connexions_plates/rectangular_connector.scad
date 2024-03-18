// v1
// Pour raccorder 2 V-slots
// arrondir les angles
// Enlever 1 mm sur les bords pour éviter les frottements. 

include <./MCAD/boxes.scad>
// exemple !
// roundedBox([20, 30, 40], 2, true);
A_x = 20;
B_y = 40;

edge = 0.5 ; // enlever cette valeur des bords.
// epp = 4 ;

dia = 5 ;  // diameter of holes
eps = 0.01 ; 


module connector(A, B, epp){
    difference() {
    // cube([A_x, B_y, epp]);
        translate([A/2, B/2, epp/2])
    roundedBox([A - (2* edge), B -(2 * edge), epp], 2, true, $fn=20);
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

module narrow_connector(){
    connector(A_x, B_y, epp = 4); 
};

module join(){
    connector(A_x, B_y, epp = 0.8); 
}

// narrow_connector();
join();



// connector();

