//###################################################
// rib1.scad
// (c) 2021 - Roie R. Black
//***************************************************
include <../../wing.data>

use <MMlib/circle_template_rib.scad>

module rib1() {
    circle_template_rib(r1c, camber, spar_size, rib_thickness);
}

rib1();

