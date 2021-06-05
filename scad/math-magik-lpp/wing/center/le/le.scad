//########################################
// le.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../../wing.data>

use <MMlib/square_spar.scad>

module le() {
  square_spar(center_span, spar_size);
}

le();

