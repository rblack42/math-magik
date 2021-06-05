use <function_grapher.scad>;
include <center-cover-points.data>
include <colors.scad>

thickness = 0.001;
style = "FACES";  // LINES to show surface grid

module center_covering() {
  color(GLASS_Blue)
  function_grapher(g_pts, thickness, style);
}
center_covering();
