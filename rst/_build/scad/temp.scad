$fn=100;

module combo() {
    union() {
        translate([0,-0.5,-0.5])
            cube([5,1,1]);
        sphere(r=2);
    }
}

combo();
translate([0,7,0])
    combo();