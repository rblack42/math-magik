//########################################
// rib2.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../left-tip.data>

use <MMlib/square_spar.scad>

module rib2() {
  translate([(
      stab_chord - 2*stab_spar_size)/2+stab_spar_size,
      -stab_spar_size/2,
      stab_spar_size])
  rotate([0,0,90])
  square_spar(stab_chord-2*stab_spar_size, stab_spar_size);
}

rib2();

