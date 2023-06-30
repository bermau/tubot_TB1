
// time varies fro 0 to 1 and 1 to 0
function position(time) = time < 0.5
      ? 50 + (time * 432)
      : 50 + (432/2 - ((time-0.5) * 432)) ;



function pos_y_sup(time) = time < 0.5
      ? 60 + (time * 500)
      : 60 + (500/2 - ((time-0.5) * 500)) ;
union(){
    cube(size=[330, 20, 20]);
    translate(v=[0, 0, 230]){
        cube(size=[330, 20, 20]);
    };
    translate(v=[0, 340, 230]){
        cube(size=[330, 20, 20]);
    };
    translate(v=[0, 340, 0]){
        cube(size=[330, 20, 20]);
    };
    color("Orange"){
        translate(v=[20, 20, 0]){
            rotate(a=[0, 0, 90]){
                cube(size=[320, 20, 20]);
            };
        };
    };
    translate(v=[0, 0, 230]){
        color("Orange"){
            translate(v=[20, 20, 0]){
                rotate(a=[0, 0, 90]){
                    cube(size=[320, 20, 20]);
                };
            };
        };
    };
    translate(v=[310, 0, 0]){
        color("Orange"){
            translate(v=[20, 20, 0]){
                rotate(a=[0, 0, 90]){
                    cube(size=[320, 20, 20]);
                };
            };
        };
    };
    translate(v=[310, 0, 230]){
        color("Orange"){
            translate(v=[20, 20, 0]){
                rotate(a=[0, 0, 90]){
                    cube(size=[320, 20, 20]);
                };
            };
        };
    };
    color("Chartreuse"){
        translate(v=[20, 0, 20]){
            rotate(a=[0, -90, 0]){
                cube(size=[210, 20, 20]);
            };
        };
    };
    translate(v=[310, 0, 0]){
        color("Chartreuse"){
            translate(v=[20, 0, 20]){
                rotate(a=[0, -90, 0]){
                    cube(size=[210, 20, 20]);
                };
            };
        };
    };
    translate(v=[310, 340, 0]){
        color("Chartreuse"){
            translate(v=[20, 0, 20]){
                rotate(a=[0, -90, 0]){
                    cube(size=[210, 20, 20]);
                };
            };
        };
    };
    translate(v=[0, 340, 0]){
        color("Chartreuse"){
            translate(v=[20, 0, 20]){
                rotate(a=[0, -90, 0]){
                    cube(size=[210, 20, 20]);
                };
            };
        };
    };
    union(){
        translate(v=[position($t), 10, 250]){
            color("DarkOrange"){
                translate(v=[-50.0, -40.0, -20]){
                    union(){
                        translate(v=[0, 0, 20]){
                            cube(size=[100, 80, 3]);
                        };
                        translate(v=[18.0, 18.0, 4.5]){
                            union(){
                                cylinder(h=11, r=12);
                                translate(v=[64, 0, 0]){
                                    cylinder(h=11, r=12);
                                };
                                translate(v=[64, 44, 0]){
                                    cylinder(h=11, r=12);
                                };
                                translate(v=[0, 44, 0]){
                                    cylinder(h=11, r=12);
                                };
                            };
                        };
                    };
                };
            };
        }; // Y slider 1
        translate(v=[position($t), 350, 250]){
            color("DarkOrange"){
                translate(v=[-50.0, -40.0, -20]){
                    union(){
                        translate(v=[0, 0, 20]){
                            cube(size=[100, 80, 3]);
                        };
                        translate(v=[18.0, 18.0, 4.5]){
                            union(){
                                cylinder(h=11, r=12);
                                translate(v=[64, 0, 0]){
                                    cylinder(h=11, r=12);
                                };
                                translate(v=[64, 44, 0]){
                                    cylinder(h=11, r=12);
                                };
                                translate(v=[0, 44, 0]){
                                    cylinder(h=11, r=12);
                                };
                            };
                        };
                    };
                };
            };
        }; // Y slider 2
        translate(v=[position($t), -30, 250]){
            translate(v=[10, 0, 0]){
                color("Purple", 0.5){
                    rotate(a=[0, 0, 90]){
                        cube(size=[460, 20, 20]);
                    };
                };
            };
        }; // Y axis
    }; // End of AXIS_Y
    translate(v=[-10, pos_y_sup($t), 3]){
        union(){
            translate(v=[position($t), 10, 270]){
                color("LightBlue", 0.8){
                    rotate(a=[0, 0, 90]){
                        translate(v=[-50.0, -40.0, -20]){
                            union(){
                                translate(v=[0, 0, 20]){
                                    cube(size=[100, 80, 3]);
                                };
                                translate(v=[18.0, 18.0, 4.5]){
                                    union(){
                                        cylinder(h=11, r=12);
                                        translate(v=[64, 0, 0]){
                                            cylinder(h=11, r=12);
                                        };
                                        translate(v=[64, 44, 0]){
                                            cylinder(h=11, r=12);
                                        };
                                        translate(v=[0, 44, 0]){
                                            cylinder(h=11, r=12);
                                        };
                                    };
                                };
                            };
                        };
                    };
                };
            }; // slider 1
        };
    }; // End of AXIS_Y_SUP
}; // End of CARCASSE
