// Fixation d'un moteur 28BYJ-48 sur une barre V-slot 20x20 

// bar
bar_y = 20;
bar_z = 20;
// petite barre de guidage
y_width_hole = 2 ;
z_width_hole = 5.5 ;

// pm : pooley_mount
pm_x = 55; 
pm_y = 3;
pm_z = 50;


module bar_20x20(){
    %cube([100, 20, 20], center = true);
};
    
module hole_m5(){
    rotate([90, 0, 0]) cylinder(h=20, r=mp_hole1_r, center = true, $fn=20);
}

module hole_m4(){
    rotate([90, 0, 0]) cylinder(h=20, r=2, center = true, $fn=20);
}

// pour fixer la monture, 2 trous de m5 distants de 10 mm.
mp_hole1_r = 5/2 ;
pm_hole1_d1 = 2 + 5;
pm_hole1_d2 = pm_hole1_d1 + 10;

module mount(){
    pm_hole2_d = 40 ; // distance de percage des trous tenant le moteur / bord droit de la mouture
    pm_hole2_distance = 35; // écart entre les trous tenant le moteur
    pm_hole2_r = 4/2;
    // motor
m_dist_to_shaft = 8 ; //
m_shaft_hole_r = 10 /2;
m_radius = (28 + 0.5) / 2; // diamètre général pour la découpe
m_pattes_defixation = 7 + 0.5;
m_profondeur = 1 ; // profondeur de la découpe pour loguer le moteur 
    
    difference(){
        // le bloc principal
        union(){
        //translate ([0, -(bar_y + pm_y)/2, 0 ])  
        cube([pm_x, pm_y, pm_z], center =true );
        
        // on ajoute une petite barre pour mieux aligner la fixation
        // translate([(pm_x-22)/2, (pm_y + y_width_hole)/2, 0])
        // cube([22, y_width_hole, z_width_hole], center = true);
        }
    // trous de fixation sur le rail
    translate ([(pm_x) /2 - pm_hole1_d1, 0, 0]) hole_m5();
    translate ([(pm_x) /2 - pm_hole1_d2, 0, 0]) hole_m5();
    // trous de fixation du moteur par 2 boulons de m4
    translate ([(pm_x) /2 - pm_hole2_d, 0, pm_hole2_distance/2]) hole_m4();
    translate ([(pm_x) /2 - pm_hole2_d, 0, -pm_hole2_distance/2]) hole_m4();
    
    // trou pour axe moteur
    translate([(pm_x/2 - pm_hole2_d + m_dist_to_shaft) ,0,  0])
    rotate([90, 0, 0]) cylinder(h=20, r=m_shaft_hole_r, center = true, $fn=20 );
    
        
    // découpe pour mieux fixer
    // un grand rond  et     // un échappement pour les fils
    d_x = 15    ; 
    d_z = 15 ;
        
    translate([(pm_x) /2 - pm_hole2_d,-(pm_y- m_profondeur)/2-0.01,0]){
        rotate([90, 0, 0]) cylinder(h=m_profondeur, r=m_radius, center = true, $fn=60);
        // zone d'échappement des fils
        translate([-20, -d_x + m_profondeur/2, -d_z/2])
        cube([d_x,d_x,d_z]);   
        // 2 petits cylindre pour loguer les pattes
        translate([0, 0, pm_hole2_distance/2])
        rotate([90, 0, 0]) cylinder(h=m_profondeur, r=m_pattes_defixation/2, center = true, $fn=20 );
        translate([0, 0, -pm_hole2_distance/2])
        rotate([90, 0, 0]) cylinder(h=m_profondeur, r=m_pattes_defixation/2, center = true, $fn=20 );
        // un petit cube pour les pattes
        translate([-m_pattes_defixation/2, -m_profondeur/2, -pm_hole2_distance/2])
      //  color("purple", 0.5) 
        cube([m_pattes_defixation,m_profondeur, pm_hole2_distance]);
        }
    // couper les parties inutiles des coins
    cut_x = 20;
    cut_y = 20;// profondeur de coupe 
    cut_h = 40; 
        // coin haut gauche
        translate([-pm_x/2, 0, +11])
        rotate([0,-45-90,0]) 
        translate([0,-15 ,-cut_h/2]) cube([cut_x, cut_y, cut_h]);     
        // coin bas gauche
        translate([-pm_x/2, 0, -11])
        rotate([0,45+90,0]) 
        translate([0,-15 ,-cut_h/2]) cube([cut_x, cut_y, cut_h]);
        
        // coin haut droit
        //rotate(
        translate([20, 0 , 20]) 
        cube([cut_h, cut_y, cut_x], center = true);
        // et son mirroir
        mirror([0,0,90]) 
        translate([20, 0 , 20]) 
        cube([cut_h, cut_y, cut_x], center = true);
        
    }; // end of diff
};

// On trace la barre

translate([-0, -0,-0]) 

bar_20x20();

// module de fixation
translate([0-55,-(bar_y+pm_y)/2, 0])
mount();
