//###################################################
// rib1.scad
// (c) 2021 - Roie R. Black
//***************************************************
include <../../stab.data>

use <MMlib/straight_rib.scad>
use <MMlib/functions.scad>

module rib1() {
  translate([r1c/2 + stab_spar_size,r1y,0])
  straight_rib(rib_radius, r1c, stab_spar_size, stab_spar_size);
}

rib1();

