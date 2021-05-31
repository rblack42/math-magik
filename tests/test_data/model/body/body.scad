use <rudder/rudder.scad>
use <stick/stick.scad>

module body() {
  union() {
    stick();
      translate([10,0,1/4])
	rudder();
  }
}
  
body();
