//########################################
// le.scad
// (c) 2021 - Roie R. Black
//****************************************
include <le.data>

use <MMlib/square_spar.scad>

module le() {
  translate([fin_spar_size/2,fin_radius + fin_le_length/2,fin_spar_size/2])
    rotate([0,0,0])
  square_spar(fin_le_length, fin_spar_size);
}

le();

