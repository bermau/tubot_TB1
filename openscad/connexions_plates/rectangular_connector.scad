// v1
// Pour raccorder 2 V-slots

A_x = 60;
B_x = 40;

A_y =A_x;
B_y= B_x;

epp = 4 ;

dia = 5 ;  // diameter of holes


module connector(){
    difference() {
    cube([A_x, B_y, epp]);
    {
        // holes on X axis
        for (i = [ 0 : 2 ]) {
          translate([10 +  i*20, 10, 0])
            cylinder(r=dia/2, h=10, $fn = 30);         
          };
        for (j = [ 0 : 2 ]) {
          translate([10 +  j*20, 30, 0])
            cylinder(r=dia/2, h=10, $fn = 30);         
          };
 
    }
    }
}


connector();

