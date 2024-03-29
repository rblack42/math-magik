//#####################################
// front-wing-post.scad
// (c) 2021 by Roie R. Black
//*************************************
include <rear-stab-post.data>
$fn=100;
use <MMlib/rounded_post.scad>

module rear_stab_post() {
  color(stab_post_color)
    translate([0,0,0])
      rounded_post(
        z1=stab_post_height,
        z2= stab_post_height-tube_height,
        t = post_diameter
      );
}

//---------------------------------------
// debug display

rear_stab_post();


