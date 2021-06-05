//########################################
// prop-spar.scad
// (c) 2021 - Roie R. Black
//****************************************
include <prop-spar.data>
$fn = 64;


module prop_spar() {
  color(prop_spar_color)
    union() {
      cylinder(
        r1=prop_spar_inner_radius,
        r2=prop_spar_outer_radius,
        h=prop_spar_length/2);
      rotate([0,180,0])
        cylinder(
          r1=prop_spar_inner_radius,
          r2=prop_spar_outer_radius,
          h=prop_spar_length/2);
    }
}

prop_spar();
