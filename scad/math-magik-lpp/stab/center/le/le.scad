//########################################
// le.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../../stab.data>

use <MMlib/square_spar.scad>

module le() {
    square_spar(stab_center_span, stab_spar_size);
}

le();

