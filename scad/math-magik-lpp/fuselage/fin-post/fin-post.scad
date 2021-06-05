//#####################################
// fin-post.scad
// (c) 2021 by Roie R. Black
//*************************************
include <fin-post.data>
use <MMlib/rounded_post.scad>

module fin_post() {
  color(post_color) {
    rotate([90,0,0])
      rounded_post(
        z1 = post_length,
        z2 = post_length-tube_height,
        t = post_size
      );
  }
}

//--------------------------------------
// debug display

fin_post();

