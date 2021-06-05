//########################################
// te.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../right-tip.data>

use <MMlib/square_spar.scad>

module te() {
  translate([stab_chord-stab_spar_size/2,-stab_tip_span/2,stab_spar_size/2])
  rotate([0,0,0])
  square_spar(stab_tip_span, stab_spar_size);
}

te();

