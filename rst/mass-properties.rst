Calculating Model Properties
############################

For this project, we will want to calculate a few basic properties of the final
design and the individual parts:

	* volume - total volume of the part or assembly

	* Weight - the design weight for the part or assembly

	* CG - the x,y,z location of the center of gravity of the part or assembly

	* Moment of Inertia - for the part or assembly

	* Bounds - the dimensions of a bounding box for the part or assembly

Most of these data items can be calculated using the **numpy-stl** package and
a bit of math. We cannot get all the data from that package because it will not
account for the material properties (specifically, the density) used in
constructing the model. However, we can calculate mass properties for each
part, then use positioning data and density information to create properties
for all parts and assemblies.

Volume
******

We can calculate the volume of each part using the associated :term:`STL` file
and the **numpy-stl** package. This needs to be multiplied by the selected
material density to calculate the actual weight of the part.

Weight
******

Designers select the "right" material for each part, and can provide the
density of that material. Much of this data needs to be entered manually, but
we can create a table of standard densities for materials like aluminum, music
wire, and covering materials that might be used. Most modelers calculate the
density of the wood materials they use.

The design weight of each part is just the material density times the volume.

Center of Gravity
*****************

The **numpy-stl** package can calculate the center of gravity for a part, but
the number they produce is based on a density of one. Once we account for the
correct material density, we need to recalculate the :term:`CG` by calculating
the moment of the part in its final position in the model. That means we need
to use the coordinate transformation data used to properly position the part in
the model.

Rotations
=========

Given a :term:`CG` location for a part, calculated by the **numpy-stl**
package. If we rotate the part, that :term:`CG` location is rotated as well,
producing a new location for the part in its new orientation.


translations
============

Moment of Inertia
*****************

The moment of inertial of a part tells us something about how that part will
move through space.

Bounds
******

The bounds of the model must be calculated to ensure the model meets the limits
spelled out in the official rules for the class the model is designed for. For
the |LPP| class, the rules limit the length of the model in an interesting way.
The measurement is made from the forwardmost point on the propeller to the
rearmost point of the model structure. These dimensions can be provided for
each part by the **numpy-stl** package
