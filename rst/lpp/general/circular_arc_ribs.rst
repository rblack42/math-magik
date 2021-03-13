Circular Arc Rib Module
#######################

Many indoor models use a simple circular arc airfoil specified using the chord
of the rib and the desired camber, which is usually expresses as a percentage
of the chord.

We need a general purpose rib module to generate the ribs. However, there is
one wrinkle that must be considered. Some ribs will be placed alongside of
leading or trailing edge spars that are sitting at some angle. Therefore, we
need two more parameters to deal with those angles.

Here is the basic module we will build:

..	code-block:: c

	module rib(l,c,ale,ate) {
		...
	}

The parameters are:

	* **l** - the chord of the desired rib (without considering aligned spars

	* **c** - the rib camber as a percentage of **l**

    * **ale** - the leading edge angle. positive if counter-clockwise when
      looking down on the top of the rib.

    * **ate** = the angle of the trailing edge spar.

    * **align** - <0 = rib should be aligned on the left, 0 - centered, >0
      alignee on the right

The **align** parameter is designed to deal with ribs that sit at the edge of a
section. Other ribs will be aligned using their centerline.

When the rib is created, it will be standing upright with the leading edge at
the origin. The rib will extend along the **x** axis, The wing is assumed to
run parallel to the **y** axis, with **z** measured upward.




