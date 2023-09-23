
module barre20_20(){
    cube([100,20,20]);
}

module mount_sg90(){
    difference(){
        cube([32.1, 40, 5]);
        
        translate([2, 14, -1]) cylinder(d=3, h = 15, $fn=30);
        translate([30, 14, -10]) cylinder(d=3, h = 25, $fn=30);
        }
}



%barre20_20();
translate([11.1 +20,-6.2,2.5])
import("cadmodel-sg90/sg90.stl");

color("purple", 0.5)translate([15,-20,20]) mount_sg90();
