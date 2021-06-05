//########################################
// te.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../../stab.data>

use <MMlib/square_spar.scad>

module te() {
  translate([stab_chord-stab_spar_size/2,0,0])
  rotate([0,0,0])
  square_spar(stab_center_span, stab_spar_size);
}

te();

