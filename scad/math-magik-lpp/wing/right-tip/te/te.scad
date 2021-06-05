//########################################
// te.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../right-tip.data>

use <MMlib/square_spar.scad>

module te() {
  translate([chord-spar_size/2,-span/2,spar_size/2])
  rotate([0,0,0])
  square_spar(span, spar_size);
}

te();

