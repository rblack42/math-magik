//###################################################
// rib2.scad
// (c) 2021 - Roie R. Black
//***************************************************
include <../../wing.data>

use <MMlib/circle_template_rib.scad>

module rib2() {
    circle_template_rib(r2c, camber, spar_size, rib_thickness);
}

rib2();

