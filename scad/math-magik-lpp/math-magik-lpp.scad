//####################################
// math-magik-lpp.scad
// (c) 2021 - Roie R. Black
//************************************
include <MMlib/functions.scad>
include <fuselage/fuselage.data>
include <prop/prop.data>
include <stab/stab.data>

use <prop/prop.scad>
use <fuselage/fuselage.scad>
use <wing/wing.scad>
use <stab/stab.scad>

pos_wing = [wing_offset+fuse_offset,-4/32,wing_elevation-1/8];
pos_stab = [srp_offset+prop_forward_x-stab_chord-3/64,-1/32,3/8];
pos_prop = [-prop_x_offset+1/64,0,-prop_z_offset,-40,0,0];

module spinning_prop(ang=$t*360) {

  color(WOOD_Balsa)
     align(pos_prop)
      rotate([-ang,0,0])
        prop();
}

module math_magik_lpp() {
  fuselage();
  position(pos_wing) wing();
  position(pos_stab) stab();
  spinning_prop();
}

//-------------------------------------
// debug display

math_magik_lpp();

