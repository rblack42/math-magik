//###################################################
// rib3.scad
// (c) 2021 - Roie R. Black
//***************************************************
include <../../wing.data>

use <MMlib/circle_template_rib.scad>

module rib3() {
    circle_template_rib(r3c, camber, spar_size, rib_thickness);
}


rib3();

