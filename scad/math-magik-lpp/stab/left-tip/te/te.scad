//########################################
// te.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../left-tip.data>

use <MMlib/square_spar.scad>

module te() {
  translate([stab_chord-stab_spar_size/2,-tip_span/2,0])
  rotate([0,0,0])
  square_spar(tip_span, stab_spar_size);
}

te();

