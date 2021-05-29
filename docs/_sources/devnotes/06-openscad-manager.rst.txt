Step 6: OpenSCAD Manager
########################

Most of the analysis of a design will be done using an :term:`STL` file which
describes a part we create. Before we worry about generating the parts, we can
set up a |PY| class that will manage access to OpenSCAD_ from the command
line.

Feature 2: Add OpenSCAD Management class
****************************************

The primary purpose of the OpenSCAD_ manager class is to isolate running
OpenSCAD to perform needed operations. For our first test of this class, we
will launch OpenSCAD and fetch the version of the program we are using.
Unfortunately, getting the |CI| servers to install the version I have on my
machine (installed with Homebrew_) has proven difficult, so we will not test the
actual version, just ensure we get valid output.

The code we need to write will assume that OpenSCAD is on the system path and
can be launched with the name :program:`openscad`. 

Here is our first test for this cloass:

..	literalinclude::	../../tests/test_OpenSCAD.py
	:linenos:
	:caption: tests/test_OpenSCAD.py


And here is the start of our class:

..	literalinclude::	../../mmdesigner/OpenSCAD.py
	:linenos:
	:caption: mmdesigner/OpenSCAD.py

With this running locally, we now need to modify the |CI| service control files
and get |OSC| installed on their *virtual machines* for testing. This took some
research, but i finally managed to get things working.


