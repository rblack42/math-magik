//###################################################
// rib3.scad
// (c) 2021 - Roie R. Black
//***************************************************
include <../../stab.data>

use <MMlib/straight_rib.scad>
use <MMlib/functions.scad>

module rib3() {
    straight_rib(rib_radius, r3c, stab_spar_size, stab_spar_size);
}

rib3();

