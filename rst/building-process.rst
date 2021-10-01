Building an Indoor Model
########################

We do not actually have a plan to work from yet, but pretend we do. How will
you proceed in building this model? Let's walk through a typical building
process, just to get a feel for the way we design indoor models. This
discussion will help us figure out a reasonable way to create our 3D model
later.

1. Clear off your workspace
***************************

Simple! We start off by picking some flat surface we will use for building. I
use a sheet of tempered glass to do my building work. I will place the plan on
this glass surface and cover it with parchment paper so glue does not stick to
the plans.

2. Lay out your plan
********************

For now, we will imagine placing a clean white paper page big enough to handle the
complete airplane. We will draw two lines on this page. One runs from the nose
of the airplane to the tip of the tail. The fuselage of our airplane will be
placed on this line. We will call this the **X axis**. Perpendicular to this
line, we draw another one that runs long enough to reach from wing tip to wing
tip (with the wing flat - no dihedral. We will call this one the **Y axis**.
There will be a third axis, one we cannot draw, that runs perpendicular to both
of these two axes. We will call this one the **Z-axis**. The origin of this
*coordinate system* is at the tip of the nose where all three axes come
together. If this all sounds familiar, it is probably because you took geometry
in high school! All measurements we will need to build our model will be
defined in this system.

3. Gather your materials:
*************************

	* Balsa wood sheet stock

    * balsa wood strip stock (maybe you cut this from sheet stock with a
      suitable stripping tool)

	* Wire for the prop shaft, bearing, and rear hook

	* Tissue to build paper tubes for mounting

    * Mylar film for covering

	* Glue (We will not be gluing anything for a while)

	* Cutting and sanding gadgets

	* An accurate measuring tool - ruler, digital caliper, etc.

    * I digital scale for measuring weights. (Mine is accurate to one
      milligram.)

4. Build the Fuselage
*********************

We will might start off by building the fuselage of our model. This involves a motor
stick, tail boom, and mounting posts for the flying surfaces.

4.1. Motor Stick
================

	* Cut a rectangular strip for the basic stick.

	* Trim it as needed using a knife blade

4.2. Tail Boom
========================

	* Again, cut a basic strip.

	* Trim it as needed using a knife blade

4.3. Mounting posts for the wing and stab
=========================================

	* Cut square posts with rounded tops where we will mount the flying
	  surfaces

	* Sand the top part round for mounting tubes which will make the connection

4.4. Glue the wing and stab posts in place
******************************************

This involves identifying where each post will go. On my design the posts are
in front of the leading edge and behind the trailing edge of each flying
surface.

..  note::

    You might notice that having the wing and stab available when we do this
    will be handy. What that means is that we might be building things in a
    somewhat random order. There is not one right way to do this!


4.5. Attach front bearing and rear hook
***************************************

This will involve bending the wire parts, and attaching then to the motor stick
centered to handle the loads imposed by the rubber motor.

4.6. Attach tail boom to motor stick
====================================

Some builders use a butt joint for this, but I will use a bit of overlap and
glue the tail boom to the side of the motor stick.

5. Build the Wing
*****************

The wing is fairly easy, unless you really want to get into weight savings by
using double-tapered spars. For now, let's just use strip stock with constant
thickness. Our wing will have a flat rectangular center section with five ribs,
and wing tips tilted up to provide needed dihedral for stability. The wing will
be constructed flat, covered, then dihedral will be added as a final step. We
will use a simple circular arc airfoil, common in many indoor models. These may
be formed by bending strip stock, or cut from sheet stock.

5.1. Wing spars
===============

We will use a rectangular center section meaning that the leading and trailing
edges are straight in the center section.  The wing tips are going to be
rounded at the forward tips. That means we will need to bend the spars around a
template of some sort. (We will generate this template in our work with
|OSC|_.) Some builders like to use a full wing template to assemble the wing

5.2. Wing Ribs
==============

The ribs are all identical circular arcs. Each rib will have a specified chord
length, and camber. It will also have a specified strip height and thickness. We
will not worry about how these ribs are formed. They could be cut from sheet
balsa, or bent around a form.

6. Build the Stabilizer
***********************

The stabilizer is going to be designed in the same was as the wing. However, we will use fewer ribs (three) and there i no tip dihedral in this design.

7. Build the Vertical Fin
*************************

This part looks exactly like the tip of the stabilizer, except we will add
another rib to close the outline. Once covered, this will be glued to the tail
boom.

8. Build the Propeller
**********************

For the |LPP| class, the propeller must be constructed using sheet balsa.
Normally, the builders cut the bladed of the propeller and sand these blanks
down so they have somewhat of an airfoil cross section, and are lighter. These
blades are then wetted and formed over a form of some sort to give then
something of a normal propeller form. Quite often that form is a simple can or
tapered coffee cup.

..  note::

    Obviously, we cannot do this in |OSC|_, but I came up with a simple way to
    create a propeller blade that will be close to what we might build. We will
    see that in the actual model design notes.

Finally, these blades are glued to a wood spar to provide the desired pitch,
and the wire drive shaft is glued in place to complete the propeller.

9. Cover the Model
******************

In this step, we use a thin mylar film to cover the flying surfaces. Actually
doing this is something of an art form involving thin mists of spray contact
cement and gingerly dripping a pre-glued structure onto a piece of film
attached to a wooden frame. Then the covered model structure is cut loose using
a razor blade of soldering iron. (I said it was an art form!)

Generating a 3D model of this covering turned out to be fairly simple once I
found a neat piece of |OSC|_ code created by `Justin Lin`_. More on that later.

10. Assembling the Model
************************

Assembling the completed model is pretty easy. The propeller drive shaft fits
into the support bearing on the motor stick. The wing and stab are connected to
the mounting posts using paper tubes that slide tightly over the mounting
posts. Once all of these connections are made, all that remains is to create a
suitable rubber motor, wind it up and turn it loose to watch it fly.

Well, actually, it is not quite that simple. There is always a lot of fine
tuning to get a model to fly the way it needs to, and picking the right
combination of propeller and rubber motor is yet another piece of art work in
this kind of competition event.

Wrapping Up
***********

Seasoned modelers can put together a new model in a matter of hours, most of
that time spent in cutting strips of wood and gluing things together. I have
even seen it done in the middle of a multi-day competition event!

Our goal here was just to get a feel for the parts we need to design and how
those parts are combined to create the final model. We will need to generate
code for each part and generate more code showing how those pars are connected
to form the major components of the model. On last count there were over 70
parts in my |LPP| design, so we have a fair amount of work to do!

