//########################################
// rib1.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../left-tip.data>

use <MMlib/square_spar.scad>

module rib1() {
  translate([
      radius+(stab_chord - radius)/2 -stab_spar_size/2,
      -tip_span+stab_spar_size/2,
      stab_spar_size/2
  ])
    rotate([0,0,-90])
      square_spar(stab_chord-radius-stab_spar_size, stab_spar_size);
}

rib1();

