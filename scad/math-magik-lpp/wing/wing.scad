//#####################################
// wing.scad
// (c) 2021 by Roie R. Black
//=====================================
include <./wing.data>
include <colors.scad>
include <MMlib/functions.scad>


use <./center/center.scad>
use <./left-tip/left-tip.scad>
use <./right-tip/right-tip.scad>
use <MMlib/paper_tube.scad>



module wing() {
  center();
  align(pos1) right_tip();
  align(pos2) left_tip();
  color("yellow") {
    position(pos3) paper_tube(r=1/32, h=1/8, t=1/64);
    position(pos4) paper_tube(r=1/32, h=1/8, t=1/64);
  }

}


//-------------------------------------
// debug display

projection(cut=false) wing();
