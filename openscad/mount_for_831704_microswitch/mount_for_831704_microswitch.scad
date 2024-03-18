// mount for microswitch 83170.4
// orignal switch has 2.25 mm holes.abs
// this has been adaptated to metric m3.

// data are Adaptated from https://docs.rs-online.com/56c1/A700000008608173.pdf
// replaced 2 holes by a single one
// used rounded boxes

include <./MCAD/boxes.scad>


x_l = 20  + 27 ;
x_4 = 20  ; // where starts the first hole
x_sliding = 13 ; // sliding zone

$fn= 32;

y_l = 20 ;
y_hole_to_edge = (9.6 - 2.4 ); 
y_d1 = y_l - y_hole_to_edge ;
y_d2 = y_hole_to_edge  ;


dia = 3 ;  // The original hole (2.25 mm) have been enlarged to 3 mm.

z_h = 3 ; 


module rainure_y(l){
    long = 6.1;  
    h = 1.7;
    
    rotate([-90,0,0])
    translate([-long/2, 0,0])
    linear_extrude(height=l)
    polygon([[0,0], [long, 0],[long - h, h], 
    [h, h ]]);
}

module hole( dia = 2, pos= [0,0,0]){
    translate(pos)
    translate([0,0,-5])
    cylinder(h= 10, r= dia/2);
}

module mount(){
    difference(){
    union(){
        translate([x_l/2, y_l/2, z_h/2])
        roundedBox([x_l, y_l, z_h], 2, true, $fn=20);
     }
    // holes for the switch
       hull(){
    hole(dia= dia, pos = [x_4, y_d1, 0 ] );
    hole(dia= dia, pos = [x_4+x_sliding, y_d1, 0 ] );
    };
    hull(){
           hole(dia= dia, pos = [x_4 + 9, y_d1,0]);
           hole(dia= dia, pos = [x_4 + x_sliding + 9, y_d1,0]);
    }
    hull(){
     hole(dia= dia, pos = [x_4, y_d2, 0 ] );
     hole(dia= dia, pos = [x_4 + x_sliding , y_d2, 0 ] );
        
        }
    hull(){
        hole(dia= dia, pos = [x_4 + 9, y_d2,0]);       
        hole(dia= dia, pos = [x_4 + 9 + x_sliding, y_d2,0]);       
        
        }

    // holes for V-slot M5 nuts
        hole(dia= 5, pos= [10, 4, 0]);
        hole(dia= 5, pos= [10, 16, 0]);
        }
}

mount();