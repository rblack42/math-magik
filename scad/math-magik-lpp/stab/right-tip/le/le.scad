//########################################
// le.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../right-tip.data>

use <MMlib/square_spar.scad>

module le() {
  translate([stab_spar_size/2,-tip_le_length/2,stab_spar_size/2])
    //rotate([0,0,0])
  square_spar(tip_le_length,stab_spar_size);
}

le();

