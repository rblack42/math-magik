//########################################
// rib1.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../right-tip.data>

use <MMlib/square_spar.scad>

module rib1() {
  translate([
      radius+(chord - radius)/2 -spar_size/2,
      -span+spar_size/2,
      spar_size/2
  ])
    rotate([0,0,-90])
      square_spar(chord-radius-spar_size, spar_size);
}

rib1();

