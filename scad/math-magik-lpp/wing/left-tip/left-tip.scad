//#####################################
// left-tip.scad
// (c) 2021 by Roie R. Black
//=====================================
include <colors.scad>

use <./arc/arc.scad>
use <./le/le.scad>
use <./te/te.scad>
use <./rib1/rib1.scad>
use <./rib2/rib2.scad>
use <./arc/arc.scad>
use <./left-tip-covering/left-tip-covering.scad>

module left_tip() {
  color(WOOD_Balsa) {
    le();
    te();
    arc();
    rib1();
  }
  //rotate([180,0,0]) left_tip_covering();
}


//--------------------------------------
// debug display

left_tip();

