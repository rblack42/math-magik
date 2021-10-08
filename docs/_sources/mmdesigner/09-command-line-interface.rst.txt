Step 9: Command Line Interface
##############################

At this point, we have enough parts to tie things together with a :term:`command line
interface`. This will make the application useful enough to release.

There are a number of ways to build a :term:`CLI` in Python. For this project,
we will use the Click_ package to simplify the code needed.

CLI Setup
*********

The first thing we need to do is establish how this application will be
configured for the user. Basically, we will add code to the **mmdesigner**
package that can be activated this way:

..	code-block:: shell

	$ python -m mmdesigner

This will start up the basic application. The full application will accept a
number of arguments after that command to define exactly what we want to
happen. We will get to that. For now, let's set up the code to respond to the
user what the basic command is used

..  note::

    Real users will not need to type n this command, we will simplify things
    greatly later.

Create the Entry Point
**********************

We will be writing a single file, **cli.py**, which will define the entry point
for the application. That entry point will be a function named **cli**. To
launch that method, we need to add a **__main__.py** file:


..	literalinclude::	../../mmdesigner/__main__.py
	:language: python
	:linenos:

This file will be activated by |PY| when we run the command shown above.

Command Flow
************

We will show the command line options using a :term:`railroad diagram`
commonly used when defining languages. They look a bit like model railroad
tracks, with switches and loops. The basic idea is simple enough. You will see
a number of diagrams, each defining a rule of some kind. The top-level rule is
where you start. You start "traveling" along that top-level rule. If you
encounter a rounded box, you type exactly what is seen in the box. If you
encounter a switch (branch) you can choose to go either way. If you encounter a
rectangular box, well there is another rule you jump to and follow that track
until you get to the end. Return to the rule you left to get to this rule. When
you get to the end of the top-level rule, the command is complete: press
:kbd:`Enter`

Basic Command Format
====================

Program Commands
================

Versions
--------

This command displays the program version, and the version data for |OSC|_,
|PY|_,  and numpy-stl_ required to perform analysis work on the design.

STL
===

This command runs |OSC|_ to generate :term:`STL` files. Normally, only part
files are processed. However adding an **--all** option will force generation
of :term:`STL` files for assemblies as well. Be warned that these can take some
time to generate, and may fail if your design is not well structured.

Some parts may take some time to process. For that reason, the program
calculates a hash code for each part :term:`SCAD` file, and checks that code when
asked to generate an :term:`STL` file. If the hash code has not been changed,
indicating a change in the design, then a new :term:`STL` file will not be
produced.

Properties
==========

Generating the properties of all the design parts requires having generated
:term:`STL` files first. If you ask for properties and the :term:`STL` file is
missing, it will be generated.  Normally, this command just processes part
files, however you can add an **--all** option after the command to force
generating properties for assemblies as well. The center of gravity
calculations for assemblies will be wrong initially since |OSC| assumes all
materials have a unit density. The **cog** command generates a correct estimate
of the center of gravity based on design densities recorded for each part.

Center of Gravity
=================

The **cog** command examines the material properties specified for each part
and calculates the correct center of gravity for the complete design. This
command also calculates the moment of inertial tensor for the design, however
that data is not used at present. It will be used in performance analysis to be
added to this project later.


Excel
=====

The **excel** command generates an Excel spreadsheet containing all the
property data for parts and assemblies found in the design. Be careful with
this spreadsheet.  It is not formatted nicely, and any changes you make to it
will be lost when you run this command again. I suggest copying it to another
place on your system if you want to modify it.

The spreadsheet will set up the calculations needed to determine the center of
gravity. If the design material properties have been set, those will be
included in the spreadsheet. Otherwise a unit density will be used in the
spreadsheet.
