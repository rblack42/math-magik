//########################################
// te.scad
// (c) 2021 - Roie R. Black
//****************************************
include <te.data>

use <MMlib/square_spar.scad>

module te() {
  translate([fin_chord-fin_spar_size/2,fin_span/2,fin_spar_size/2])
  square_spar(fin_span, fin_spar_size);
}

te();

