//########################################
// arc.scad
// (c) 2021 - Roie R. Black
//****************************************
include <arc.data>

use <MMlib/circular_arc_spar.scad>

module arc(r=fin_radius, size=fin_spar_size) {
  translate([r,r,0])
  circular_arc_spar(r, 180,270, size,size);
}

arc();

