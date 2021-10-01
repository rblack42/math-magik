SCAD Component Files
####################

Our design will be made up of a set of *components*. These *components* will
either be assemblies made up of other *components*, or individual *parts* which
we will manufacture. All *components* will have a name, which will be used in
several ways.

Component Directories
*********************

Every *component* we create in our airplane design will be saved in a directory
somewhere in the project directory tree. This directory will be named to
indicate what the component is, and will contain a single SCAD file describing
that component shape. In addition, there will be a second SCAD file with the
component name followed by **_data**. This name will be used to check for
various component properties when we process the design files later.

If the component is a part, meaning something we would actually build, then there
will be no subdirectories in this component directory. On the other hand, is this
component is an assembly, each required dependent component will be stored in a
subdirectory named after that dependent component.

This structure can continue down until there are only parts remaining. The
resulting tree-like structure of this system models how we build our airplanes.
We break the overall design into major sections like a wing of a fuselage, then
we break the wing down into fundamental parts like the leading and trailing
edges and the ribs. When we build the airplane, we start by collecting all
dependent parts to build an assembly, then we gather some assemblies to build
larger assemblies until we finish the model.  In essence, we are traversing this
directory structure from the bottom where the parts live up to the top where
the finished model lives.

Connecting Objects
******************

Objects in this system are either glued to other components, or assembled using
something like paper tubes for our indoor models, or rubber bands for other
kinds of models.

If they are glued, it will be important that our models line up properly. We
will calculate the amount of glue required by nudging one component "into" a
second component (which is actually a part) and calculating the intersection of
the two component shapes. This will give us an estimate of the amount of glued
required at this joint.

Object Shape Files
******************

All components will have a single **scad** file which contains the OpenSCAD_
commands needed to generate that component. Some components use only OpenSCAD_
primitive shapes, but others might use library files stored in the projects
**MMlib** directory.

Object Position and Orientation
===============================

Every component will have a defined point which we will place at the origin of our
coordinate system. when we write our shape code. When we assemble a part into an
assembly, we will need to define a position and orientation for the actual part.
We will  use a simple convention for this.

Object Coordinate system
------------------------

The coordinate system we will use is a simple 3D Cartesian system. For us
aviation folks, assume you are sitting at the origin in an airplane looking out
toward the nose. You are looking along the negative **X** axis. The positive
**Y** axis is out your right window, and the **Z** axis is up. We will keep
this reference system in mind when we generate parts, and hopefully orient our
parts in a way that makes sense for the design.

Rotations are also needed, so we need to define those as well. All rotations
use something called the *right-hand rule*. You take your right hand and point
the thumb along each of the positive coordinate axes. A positive rotation would
follow the curl of your right-hand fingers around your thumb. That means a
positive rotation along the **X** axis would roll the airplane to the left.
(Think about it!) A positive rotation around the **Y** axis would pitch the
nose up. (You should be able to figure out rotations around the **Z** axis!)

Parts do not know anything about where they will end up in the  design. All we
need to do is identify a reference point for each part. When we assemble a part
into a larger component, we will need to define the position and orientation of
the part in its place in the assembly. When we join assemblies into larger
assemblies we will do the same thing: establish a reference point for the
smaller assembly, then define the position and orientation of that assembly in
the larger assembly.

Object Data Files
*****************

Each component directory will contain a component data file which defines any
parameters needed to manufacture the part. These files are named
**componentname_data.scad**.

Object Specific Data
====================

Some data parameters will define part specific dimensions. The values chosen
for these dimensions are usually design decisions. As much as possible these dimensions will be the only place you will see raw numbers. These will look something like this:

..  code-block:: c

    stab_span = 18.0;

Here, we are defining a value and giving that value a name. We will use that
name in other places, in mathematical expressions needed to calculate some
other value.


Component Derived Dimensions
============================

Many dimensions must be calculated based on other dimensions found in some
other data file. We will **include** those data files to provide access to the
needed named values.

Every component will be located in a directory with that component name. In
that directory we will create a design file that creates part of the actual
model. There will also be a data file with the same name, but ending with
**_data.scad**. We will include this data file in the associated design file to
make al the needed dimensions available when creating the part or assembly.

Material Properties
===================

All part component data files will contain material property values as well. These
will always include:

	* **color** - derived from the project **colors.scad** file.

	* **density** the weight per cubic foot of the selected material.

If either of these two values is missing, project defaults will be used.

Other properties can be included as needed.

Position and Orientation
========================

Finally, all assembly data files will contain position and orientation
definitions for all dependent components. These values will be used when
positioning the dependent components as we create the assembly. These position
files all are named with the component name and end with **_pos.scad**.

Hopefully, this description will help you locate data needed to understand the
design. 

I hope to streamline a lot of this when the final design application is created
later in these notes.



