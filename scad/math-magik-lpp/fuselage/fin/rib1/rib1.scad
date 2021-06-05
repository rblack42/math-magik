//########################################
// rib1.scad
// (c) 2021 - Roie R. Black
//****************************************
include <rib1.data>

use <MMlib/square_spar.scad>

module rib1() {
  translate([fin_radius+(fin_chord - fin_radius)/2 -fin_spar_size/2,fin_spar_size/2,fin_spar_size/2])
  rotate([0,0,90])
  square_spar(fin_chord-fin_radius-fin_spar_size, fin_spar_size);
}

rib1();

