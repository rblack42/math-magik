//###################################################
// rib1.scad
// (c) 2021 - Roie R. Black
//***************************************************
include <../../wing-data.scad>

use <MMlib/straight_rib.scad>
use <MMlib/functions.scad>

module rib1() {
    straight_rib(rib_radius, r1c, spar_size, spar_size);
}

rib1();

