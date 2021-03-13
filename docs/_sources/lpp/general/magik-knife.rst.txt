The Magik Knife
###############

Much of your job as a builder of model airplanes involves trimming away chunks
of material you do need from chunks you do need! For example, when building a
motor stick for a rubber-powered craft, you might start off with a simple block
that has a defined length, height, and thickness. Perhaps the height
and thickness match some standard size of Balsa available at you local supply
store. If not, and you are lucky enough to own something like a Byrnes Table
Saw, you can cut this basic stick on your saw from sheet balsa stock. If you
are extremely luck, you slice it out of the sheet with your laser cutter! (Balsa
is cheap, our tools are not!)


But wait! What if we want to trim off more material to taper the motor stick at the
front and rear. Now, we dig out our handy cutting device (X-Acto, razor blade,
whatever you use), line it up properly with a straight-edge ruler, and slice away the
unneeded material.

What you just did was identify two points on your motor stick blank, and align
the straight-edge using those two points. You picked up your knife and aligned
it so your cut would pass through the wood at the angle you want, then you
sliced away! You kept something (your motor stick) on one side of the blade, and
probably tossed the excess material on the other side.

OpenSCAD provides a way to do this slicing operation. All we need to do it set
up a suitable rectangular block, properly align it at two points on our stick, then use
the *difference* operation to remove the part we do not want.

To make this happen in OpenSCAD, I created a *knife* module that uses two 3D
coordinate values to define the two points we will use as our trimming guide, then three
angles to properly orient our trimming block. Finally, it uses a *side*
parameter to control which side of the cut we will keep.  Here is the basic module setup;

..	code-block::	c

	module knife(p1, p2, angle, side, blk_size) {
      ...
    }

We will use this knife by setting up a *difference* operation that identifies
the object we want to trim, and the knife to use:

..	code-block:: c

	p1 = [0,0,1/8];
	p2 = [2.0, 0, 3/8];
	angles = [90,0,0];
    size = [1,2,2];

	difference() {
		motor_stick_blank();
		knife(p1,p2,angles,"left",size);
	}

To figure out the knife angles, visualie your knife with the point sitting at
the origin, sitting flat on the Y-Z plane. Rotate the knife into the
orientation you want using angles around each coordinate axis. If your motor
stick is sitting flat on the X-Z plane, they your knofe whoult be oriented
vertical to that plane:

..	code-block:: c

	angles = [90,0,0];

The module will take care of aligning the now-vertical blade along the two
defined points.

The values for **side** are either **"left"** or **"right"**

The **blk_size** parameter sized the trimming block OpenSCAD will use to
"vaporize" the part of the object we do not want. Sizing this is important so
you are not left with artifacts from the *difference* operation.

When using this knife module, you can see the trimming block by changing the
*difference* operation to a *union* operation. This will help you choose block
size so you get the cut you want.

