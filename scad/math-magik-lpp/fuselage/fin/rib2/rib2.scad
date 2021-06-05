//########################################
// rib2.scad
// (c) 2021 - Roie R. Black
//****************************************
include <rib2.data>

use <MMlib/square_spar.scad>

module rib2() {
  translate([(fin_chord -2*fin_spar_size)/2+fin_spar_size,fin_span-fin_spar_size/2,fin_spar_size/2])
  rotate([0,0,90])
  square_spar(fin_chord-2*fin_spar_size, fin_spar_size);
}

rib2();

