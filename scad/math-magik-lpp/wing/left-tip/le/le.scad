//########################################
// le.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../left-tip.data>

use <MMlib/square_spar.scad>

module le() {
  translate([spar_size/2,-le_length/2,spar_size/2])
    //rotate([0,0,0])
  square_spar(le_length,spar_size);
}

le();

