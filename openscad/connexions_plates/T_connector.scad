// compatible avec https://fr.aliexpress.com/item/32963365007.html
// v1

A_x = 60;
B_x = 20;

A_y = A_x;
B_y = B_x;

epp = 4 ;

dia = 5 ;  // diameter of holes


module connector(){
    difference() {
        translate([-30,0,0])
    cube([A_x, A_y, epp]);
    {
        // holes on X axis
        for (i = [ 0 : 2 ]) {
          translate([-20 +  i*20, 10, 0])
            cylinder(r=dia/2, h=10, $fn = 30);         
          };
        // holes for Y axis
        for (j = [ 0 : 1 ]) {
          translate([0, 30 +  j*20,  0])
            cylinder(r=dia/2, h=10, $fn = 30);         
        }
        
        // coupes en miroir
        translate([10, 20, 0])
        cube([25, 40, 10]); 
        mirror([90, 0, 0 ])
        translate([10, 20, 0])
        cube([25, 40, 10]); 
        
        
        
//        // coupure en biais
//        
//        translate([40,40,0])
//        rotate([0,0,45+90])
//        translate([0, -15, 0])
//        cube([100,30, 20], center= true);
        
    }
    }
}


connector();

