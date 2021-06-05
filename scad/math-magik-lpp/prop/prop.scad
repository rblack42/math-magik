//######################################
// prop.scad
// (c) 2021 - Roie R. Black
//**************************************
include <MMlib/functions.scad>
include <prop.data>

use <./prop-blade-1/prop-blade-1.scad>
use <./prop-blade-2/prop-blade-2.scad>
use <./wire-shaft/wire-shaft.scad>
use <./prop-spar/prop-spar.scad>


module prop() {
  align(pos_blade1) prop_blade_1();
  align(pos_blade2)  prop_blade_2();
  prop_spar();
  position(pos_wire_shaft) wire_shaft();
}

//---------------------------------------
// debug display
prop();
