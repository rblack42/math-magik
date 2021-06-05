//#####################################
// fin.scad
// (c) 2021 by Roie R. Black
//*************************************
include <fin.data>
use <MMlib/paper_tube.scad>

use <./arc/arc.scad>
use <./le/le.scad>
use <./te/te.scad>
use <./rib1/rib1.scad>
use <./rib2/rib2.scad>
use <./arc/arc.scad>
use <./fin-covering/fin-covering.scad>


module fin() {
  translate([0,0,-fin_span])
    rotate([90,0,0]) {
      color(fin_color) {
        union() {
          le();
          te();
          rib1();
          rib2();
          arc();
        }
      }
      translate([0,2,1/32]) rotate([180,0,0]) fin_covering();
      color("yellow")
        translate([fin_chord+1/32+1/64,fin_span-3/64,-3/64])
          paper_tube(r=1/32, h=1/8,t=1/64);
    }
}

//--------------------------------------
// debug display

fin();

