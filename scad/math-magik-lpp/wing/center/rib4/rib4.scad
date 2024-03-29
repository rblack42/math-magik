//###################################################
// rib4.scad
// (c) 2021 - Roie R. Black
//***************************************************
include <../../wing.data>

use <MMlib/circle_template_rib.scad>

module rib4() {
    circle_template_rib(r4c, camber, spar_size, rib_thickness);
}

rib4();

