use <function_grapher.scad>;
include <left-tip-covering-points.data>
include <colors.scad>

thickness = 0.001;
style = "FACES";  // LINES to show surface grid

module left_tip_covering() {
  color(GLASS_Blue)
  function_grapher(g_pts, thickness, style);
}


left_tip_covering();
