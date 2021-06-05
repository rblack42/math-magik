use <function_grapher.scad>;
include <right-tip-covering-points.data>
include <colors.scad>

thickness = 0.001;
style = "FACES";  // LINES to show surface grid

module right_tip_covering() {
  color(GLASS_Blue)
  function_grapher(g_pts, thickness, style);
}
right_tip_covering();
