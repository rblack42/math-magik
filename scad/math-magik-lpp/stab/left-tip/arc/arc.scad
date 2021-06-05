//########################################
// arc.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../left-tip.data>

use <MMlib/circular_arc_spar.scad>

module arc(r=radius, size=stab_spar_size) {
  translate([r,-tip_span+r,0])
    circular_arc_spar(r, 180,270, size,size);
}

arc();

