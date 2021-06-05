//#####################################
// motor-stick.scad
// (c) 2021 - Roie R. Black
//*************************************
include <colors.scad>
include <motor-stick.data>


module motor_stick() {
  color(WOOD_Balsa)
    rotate([90,0,0])
      translate([0,0,-ms_thickness/2])
	  linear_extrude(
	      height = ms_thickness,
	      center=false,
	      convexity=10
	  )
        polygon(ms_points);
}

//-------------------------------------
// debug display

motor_stick();
