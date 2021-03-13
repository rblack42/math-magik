Covering Our Model
##################

Up to now, we have focused on building the airframe. This craft will not fly
until we cover it. These days, mylar film seems to be the covering of choice.
Some crinkle it up to remove static cling, resulting in a semi-transparent film
that is easier to see when the airplane is cruising near the ceiling.

We can generate a film surface and lay it over our airframe to give the
appearance of ths covering.

I found some nice code for this on Stephen Lin's website. Three files were used
for this work:

	* bezier_curve.scad

	* function_grapher.scad 

The first package provides tools for generating a smooth mesh of points given a
coarse mesh of a of three dimensional points. The coarse mesh is smoothed by
fitting Bezier curve through the mesh points, then using the equation for
these points to generate intermediate points.

Once we have a smooth mesh, the **function-grapher** module generates the display.

THis is great for a rectangular mesh. However, rectangular airplanes look bad, so we need to work on a scheme to handle our model.

Specifically, what do we do on he tips of our flying surfaces where we have rounded edges.

We could do what we do in real building: lay a rectangular sheet over our airframe, ansd slice off the excess!. 
