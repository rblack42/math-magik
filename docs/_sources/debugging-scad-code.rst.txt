Debugging OpenSCAD Code
#######################

There are several features available that can be used to debug your code.
Beginners often debug by adding a bit of code and processing that code to get a
ook at the results. However, that does not always work, especially when you are
trying o slice away pieces of a n object. Here are some smple tweaks you can
make to simplify debugging:

Echo Output
***********

To display the results of calculations, or to see that your code has reached a
particular spot, the **echo** command will cause display on the console at the
lower right as your code is processed:

..	code-block;; c

	x = 4;
	y = 3;
	r = sqrt(x*x + y*y);
	echo("The hypotenuse is ", r);
