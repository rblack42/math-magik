//#######################################
// prop-blade--2.scad
// (c) 2021 - Roie R. Black
//***************************************
include <colors.scad>
include <prop-blade-2.data>
use <MMlib/elliptic_blade_blank.scad>

$fn = 100;


module prop_form() {
	difference() {
		cylinder(
			r=prop_form_radius,
			h=prop_form_height);
    translate([0,0,-1])
      cylinder(
        r=prop_form_radius-prop_blade_thickness,
        h=prop_form_height+2);
	}
}

module prop_blade_slicer() {
  translate([0,-1,0.5])
    rotate([90,-15,0])
      linear_extrude(
        height = prop_form_radius,
        center = false,
        convexity = 10
      )
        elliptic_blade_blank(s,c,f,s1,s2,s3,s4);
}

module prop_blade_2() {
  color(prop_blade_color)
    rotate([0,15,-60])
      translate([0,prop_form_radius,0]) {
        intersection() {
          prop_form();
          prop_blade_slicer();
        }
      }
}

prop_blade_2();
