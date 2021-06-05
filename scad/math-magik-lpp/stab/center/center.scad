//#####################################
// stab_center.data
// (c) 2021 by Roie R. Black
//=====================================
include <../stab.data>
include <colors.scad>

use <./le/le.scad>
use <./te/te.scad>
use <./rib1/rib1.scad>
use <./rib2/rib2.scad>
use <./rib3/rib3.scad>
use <./center-covering/center-covering.scad>


module center() {
  color(WOOD_Balsa) {
    le();
    te();
    position(pos1) rib1();
    position(pos2) rib2();
    position(pos3) rib3();
  }
  position(pos_cov) center_covering();
}

//-------------------------------------
// debug display
center();

