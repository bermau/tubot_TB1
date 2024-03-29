
// time varies fro 0 to 1 and 1 to 0
function position(time) = time < 0.5
      ? 50 + (time * 1372)
      : 50 + (1372/2 - ((time-0.5) * 1372)) ;



function pos_y_sup(time) = time < 0.5
      ? 60 + (time * 500)
      : 60 + (500/2 - ((time-0.5) * 500)) ;
union(){
    cube(size=[800, 20, 20]);
    translate(v=[0, 0, 280]){
        cube(size=[800, 20, 20]);
    };
    translate(v=[0, 380, 280]){
        cube(size=[800, 20, 20]);
    };
    translate(v=[0, 380, 0]){
        cube(size=[800, 20, 20]);
    };
    color("Orange"){
        translate(v=[20, 20, 0]){
            rotate(a=[0, 0, 90]){
                cube(size=[360, 20, 20]);
            };
        };
    };
    translate(v=[0, 0, 280]){
        color("Orange"){
            translate(v=[20, 20, 0]){
                rotate(a=[0, 0, 90]){
                    cube(size=[360, 20, 20]);
                };
            };
        };
    };
    translate(v=[780, 0, 0]){
        color("Orange"){
            translate(v=[20, 20, 0]){
                rotate(a=[0, 0, 90]){
                    cube(size=[360, 20, 20]);
                };
            };
        };
    };
    translate(v=[780, 0, 280]){
        color("Orange"){
            translate(v=[20, 20, 0]){
                rotate(a=[0, 0, 90]){
                    cube(size=[360, 20, 20]);
                };
            };
        };
    };
    color("Chartreuse"){
        translate(v=[20, 0, 20]){
            rotate(a=[0, -90, 0]){
                cube(size=[260, 20, 20]);
            };
        };
    };
    translate(v=[780, 0, 0]){
        color("Chartreuse"){
            translate(v=[20, 0, 20]){
                rotate(a=[0, -90, 0]){
                    cube(size=[260, 20, 20]);
                };
            };
        };
    };
    translate(v=[780, 380, 0]){
        color("Chartreuse"){
            translate(v=[20, 0, 20]){
                rotate(a=[0, -90, 0]){
                    cube(size=[260, 20, 20]);
                };
            };
        };
    };
    translate(v=[0, 380, 0]){
        color("Chartreuse"){
            translate(v=[20, 0, 20]){
                rotate(a=[0, -90, 0]){
                    cube(size=[260, 20, 20]);
                };
            };
        };
    };
    union(){
        translate(v=[position($t), 10, 300]){
            color("DarkOrange"){
                translate(v=[-50.0, -40.0, -20]){
                    union(){
                        translate(v=[0, 0, 20]){
                            cube(size=[50, 50, 6.5]);
                        };
                        translate(v=[22.384999999999998, 22.384999999999998, 5.6]){
                            union(){
                                cylinder(h=8.8, r=7.615);
                                translate(v=[55.230000000000004, 0, 0]){
                                    cylinder(h=8.8, r=7.615);
                                };
                                translate(v=[55.230000000000004, 35.230000000000004, 0]){
                                    cylinder(h=8.8, r=7.615);
                                };
                                translate(v=[0, 35.230000000000004, 0]){
                                    cylinder(h=8.8, r=7.615);
                                };
                            };
                        };
                    };
                };
            };
        }; // Y slider 1
        translate(v=[position($t), 390, 300]){
            color("DarkOrange"){
                translate(v=[-50.0, -40.0, -20]){
                    union(){
                        translate(v=[0, 0, 20]){
                            cube(size=[50, 50, 6.5]);
                        };
                        translate(v=[22.384999999999998, 22.384999999999998, 5.6]){
                            union(){
                                cylinder(h=8.8, r=7.615);
                                translate(v=[55.230000000000004, 0, 0]){
                                    cylinder(h=8.8, r=7.615);
                                };
                                translate(v=[55.230000000000004, 35.230000000000004, 0]){
                                    cylinder(h=8.8, r=7.615);
                                };
                                translate(v=[0, 35.230000000000004, 0]){
                                    cylinder(h=8.8, r=7.615);
                                };
                            };
                        };
                    };
                };
            };
        }; // Y slider 2
        translate(v=[position($t), -30, 300]){
            translate(v=[10, 0, 0]){
                color("Purple", 0.5){
                    rotate(a=[0, 0, 90]){
                        cube(size=[500, 20, 20]);
                    };
                };
            };
        }; // Y axis
    }; // End of AXIS_Y + 2 sliders
    translate(v=[-10, pos_y_sup($t), 3]){
        union(){
            translate(v=[position($t), 10, 320]){
                color("LightBlue", 0.8){
                    rotate(a=[0, 0, 90]){
                        translate(v=[-50.0, -40.0, -20]){
                            union(){
                                translate(v=[0, 0, 20]){
                                    cube(size=[50, 50, 6.5]);
                                };
                                translate(v=[22.384999999999998, 22.384999999999998, 5.6]){
                                    union(){
                                        cylinder(h=8.8, r=7.615);
                                        translate(v=[55.230000000000004, 0, 0]){
                                            cylinder(h=8.8, r=7.615);
                                        };
                                        translate(v=[55.230000000000004, 35.230000000000004, 0]){
                                            cylinder(h=8.8, r=7.615);
                                        };
                                        translate(v=[0, 35.230000000000004, 0]){
                                            cylinder(h=8.8, r=7.615);
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
