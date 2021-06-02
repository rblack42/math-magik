$fn=100;
use <body/body.scad>
use <wing/wing.scad>
use <stab/stab.scad>

module model() {
  union() {
    body();
    translate([2,0,1/4]) wing();
    translate([10,0,-3/8]) stab();
  }
}

model();
