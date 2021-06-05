//#####################################
// center.scad
// (c) 2021 by Roie R. Black
//=====================================
include <center.data>
include <colors.scad>

use <./le/le.scad>
use <./te/te.scad>
use <./rib1/rib1.scad>
use <./rib2/rib2.scad>
use <./rib3/rib3.scad>
use <./rib4/rib4.scad>
use <./rib5/rib5.scad>
use <./center-covering/center-covering.scad>

module center() {
  color(WOOD_Balsa) {
    position(pos_le) le();
    position(pos_te) te();
    position(pos_rib1) rib1();
    position(pos_rib2) rib2();
    position(pos_rib3) rib3();
    position(pos_rib4) rib4();
    position(pos_rib5) rib5();
  }
  //translate([0,-6,0]) center_covering();
}

//-------------------------------------
// debug display
center();

