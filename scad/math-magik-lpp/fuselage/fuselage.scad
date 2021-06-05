//##########################################
// fuselage.scad
// (c) 2021 - Roie R. Black
//******************************************
include <fuselage.data>
include <tail-boom/tail-boom.data>
include <fin/fin.data>

use <motor-stick/motor-stick.scad>
use <thrust-bearing/thrust-bearing.scad>
use <rear-hook/rear-hook.scad>
use <front-wing-post/front-wing-post.scad>
use <rear-wing-post/rear-wing-post.scad>
use <tail-boom/tail-boom.scad>
use <front-stab-post/front-stab-post.scad>
use <rear-stab-post/rear-stab-post.scad>
use <fin/fin.scad>
use <fin-post/fin-post.scad>

module fuselage() {
  //adjust motor stick to fit bearing
	translate([fuse_offset,0,0]) motor_stick();
	translate([0,0,-prop_z_offset]) thrust_bearing();
  translate([ms_length+fuse_offset,0,0]) rear_hook();
  translate([fp_offset+fuse_offset,-ms_thickness,0]) front_wing_post();
  translate([rp_offset+fuse_offset,-ms_thickness,0]) rear_wing_post();
  translate([ms_length,-ms_thickness + tb_thickness/2,0]) tail_boom();
  translate([sfp_offset + prop_forward_x,-ms_thickness + 1.5 *tb_thickness,0]) front_stab_post();
  translate([srp_offset + prop_forward_x,-ms_thickness + 1.5 *tb_thickness,0]) rear_stab_post();
  fin_le_x = srp_offset-fin_chord+prop_forward_x+3/128;
  translate([fin_le_x,-tb_thickness-1/64,1/32]) rotate([0,-1.5*tail_boom_angle,-3])fin();
  translate([srp_offset+prop_forward_x+2/32,0,1/32]) fin_post();
}


//----------------------------------------------
// debug display
fuselage();
