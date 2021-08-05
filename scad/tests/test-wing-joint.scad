$fn = 360;
module wing() {
  translate([0,0,1]) {
  difference() {
    translate([0,0,-12.25]) rotate([0,90,0])
      cylinder(h=9, r= 12.5);
    translate([-1,-15,-31]) cube([12,30,30]);
  }
}
}

wing();
translate([9,0,0]) rotate([0,-30,0])  color("red") wing();