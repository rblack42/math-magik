//########################################
// rib2.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../left-tip.data>

use <MMlib/square_spar.scad>

module rib2() {
  translate([(
      chord - 2*spar_size)/2+spar_size,
      -spar_size/2,
      spar_size])
  rotate([0,0,90])
  square_spar(chord-2*spar_size, spar_size);
}

rib2();

