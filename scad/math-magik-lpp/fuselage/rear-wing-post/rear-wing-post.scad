//#####################################
// rear-wing-post.scad
// (c) 2021 by Roie R. Black
//*************************************
include <rear-wing-post.data>
$fn=100;
use <MMlib/rounded_post.scad>

module rear_wing_post() {
  color(post_color)
    translate([0,0,0])
      //rounded_post(z1=post_height);
      rounded_post(
        z1=post_height,
        z2= post_height-tube_height,
        t = post_diameter
      );
}

//---------------------------------------
// debug display

rear_wing_post();


