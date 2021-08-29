Project Goals
#############

This project started off with a few goals in mind.

Visualize the Model
*******************

Most modelers use plans to build their design. Those plans are flat and do not
really show you what the model will look like in real life. I wanted to be able
to see my design in a more realistic way. I want to be able to examine it from
any angle I choose, and zoom in to see details. OpenSCAD_ gives me exactly that
kind of capability.

Ensure Conformance to Rules
***************************

The design I come up with will not be of much value unless it conforms to the
rules. I want my design process to be able to check those constraints. By
itself, OpenSCAD_ cannot help much here. However, it is possible to
export your design into another format more suitable for making calculations
that will help.

We will export our design into something called an *STL* file (Standard
Tessellation Library) format. We can then use another tool, Python_ to process
those files to get the data I need to check conformance with the rules.

..	note::

    Python_ is another programming language, but one that is also simple enough
    that many kids manage to use it from a very early age. It is a very popular
    first language use din teaching computer programming. We will not cover
    Python in this work, but we will go over the code I generated so you can
    see how I use it in my analysis of the model design.

Estimate Model Weight
*********************

Indoor modelers sometimes obsess over the weight of things. This is no
surprise. Anything that flies needs to be light, but strong enough to hold
together under the stresses of flight. Lighter airplanes should fly longer than
heavier ones.

Again, *STL* files can be used to give us the weight estimate. If we identify
the density of the material we will use for each part used in the design, we
can add all of those up to get the overall weight. I found a nice Python
support package that will process and *STL* file and give you the total volume
of the design in that file. If we know the density of the material we will use
for that part, we cna get an estimate of the weight,

Unfortunately, estimating the weight of the glue is harder to do. To estimate
the glue weight, we need to know the surface area of the joints we will be
gluing together.  This is possible, but not completed for this project. (Yet!)

Locating Center of Gravity
**************************

We need to locate the center of gravity of our aircraft to ensure it will fly
as desired. This is again something my Python support code will give us.

Perform Aerodynamic Analysis
****************************

I trained as an Aerospace Engineer in college. I almost completed a PhD in that
discipline, but warped into a computer geek instead. I still like to work on
aerodynamics programs, and I would like to do some work on my indoor designs.
However, that part of my goals is not included in this project at the present
time.  Still having a complete computerized model of my design is a starting
point for further analysis work. Stay tuned to this channel for further
bulletins!

