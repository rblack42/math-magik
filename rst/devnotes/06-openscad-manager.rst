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

Test OpenSCAD Version
=====================

Users will need to install at least OpenSCAD version 2019.05, so we will set up
a test to check that.

Here is our first test for this class:

..  literalinclude::    ../../tests/test_OpenSCAD.py
    :linenos:
    :caption: tests/test_OpenSCAD.py


And here is the start of our class:

..  literalinclude::    ../../mmdesigner/OpenSCAD.py
    :linenos:
    :lines: 1-13
    :caption: mmdesigner/OpenSCAD.py


With this running locally, we now need to modify the |CI| service control files
and get |OSC| installed on their *virtual machines* for testing. This took some
research, but i finally managed to get things working.

Test OpenSCAD STL Generation
============================

Our next task involves getting OpenSCAD to generate an :term:`STL` file from
the associated :term:`SCAD` file.

..  literalinclude::    ../../mmdesigner/OpenSCAD.py
    :linenos:
    :lines: 14-32
    :caption: mmdesigner/OpenSCAD.py

Mass Property Generator
=======================

Now that we can generate an :term:`STL` file, we can analyze that file to get
the part properties. These will be saved in a :term:`JSON` output file:

..  literalinclude::     ../../mmdesigner/OpenSCAD.py
    :linenos:
    :caption: mmdesigner/OpenSCAD.py

This code depends on **numpy-stl** which needs to be added to the **requirements.txt** file.
