//#####################################
// stab.scad
// (c) 2021 by Roie R. Black
//=====================================
include <./stab.data>
include <colors.scad>

use <./center/center.scad>
use <./left-tip/left-tip.scad>
use <./right-tip/right-tip.scad>
use <MMlib/paper_tube.scad>

module stab() {
  center();
  translate([0,stab_center_span/2,0]) rotate([180,0,0]) right_tip();
  translate([0,-stab_center_span/2,0]) left_tip();
  color("yellow") {
    translate([-1/32-1/64,0,0]) paper_tube(r=1/32, h=1/8, t=1/64);
    translate([4+1/32+1/64,0,0]) paper_tube(r=1/32, h=1/8, t=1/64);
  }
}


//-------------------------------------
// debug display

stab();
