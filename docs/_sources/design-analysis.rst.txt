..  _design-analysis:

Design Analysis
###############

Just looking at the design we intend to build is certainly nice to be able to
do, but the real benefit of designing anything in the computer is that you can
analyze the design in a number of ways. For example, I want to be able to get
an estimate of the total weight of this design, determine where the center of
gravity will be, and make sure the overall size of the model meets the
constraints defined in the rules for the model class.

OpenSCAD_ alone will not generate any of this information directly. However,
you can *export* a design in another format, then process that data to get the results we need.

3D printers commonly use an *STL* file as part of the printing process, STL stands for Standard Tesselation Library. Tessellation is a process that wraps up an object in a system of tiny triangles connected to each other with no gaps. Triangles are nice since they are always flat and we can easily figure out geometrical properties from each one, like how big it is and its orientation. Also,  because each side is a straight line, two triangles can be alligned exactly side by side, creating a "water-tight" covering for our shape. The tesselation process gives us a new shape that is not identical to the original, but with small triangles it is pretty close. OpenSCAD will export any design or part of a design you can see on the screen. Thisis very handy for our analysis.

Organizing the Design
*********************

By now you have seen how to get your design on the screen. WHat you end up with
is many small parts placed in just the right spot so the resulting view is your
model. TO get our analysis work done, we need to see each part individually. I
decided to built a file structure what uses directories (folders to you PC
folks) and subdirectories to manage all the parts of my design. The process
looks like this:

Directory Tree
==============

Start with a folder that containing just one file: **math-magik-lpp,scad. This file generates the complete model. To build the model, this file wull *use* other **scad** files. Identify the chunks of that model that you want to make separable. I chose chunks that represent the major parts of the model that can be separated for transportation. In door models usually have removable wings, possibly stabilizers, propeller and rubber motor. Create subdirectories in the top-level directory holding your model file, one ofr each assembly each named suitably. I use names like *wing* and *stab* which are pretty obvious.

In each of these subdirectories, place *scad* files that will generate that assembly. If that assembly needs other chunks to generate, those chunks will be managed in further subdirectories. We keep going down into smaller and smaller pieces of the design until we get to basic parts we would manufacture ourselves out of our raw materials.

Here is a representation of the "directory tree" - yes it is upside down - under my top-level design directory.


..  code-block::    text

    .
    ├── fin
    │   ├── covering
    │   └── frame
    ├── fuselage
    │   ├── motor_stick
    │   ├── prop_mount
    │   ├── rudder_brace
    │   ├── stab_posts
    │   ├── tail_boom
    │   └── wing_posts
    ├── math-magik-lpp.scad
    ├── motor
    ├── power-plant
    │   ├── propeller
    │   │   ├── blades
    │   │   ├── shaft
    │   │   └── spar
    │   └── rubber_motor
    ├── propeller
    │   ├── blades
    │   ├── shaft
    │   └── spar
    ├── stab
    │   ├── center
    │   ├── covering
    │   ├── left_tip
    │   ├── mounts
    │   └── right_tip
    └── wing
        ├── wing_center
        ├── wing_covering
        ├── wing_left_tip
        ├── wing_mounts
        └── wing_right_tip

This diagram was generated using a nice open source tool, oddly called
**tree**, on my Mac.

That is a lot of directories! Each one holds an *scad* file defining that
shape, and any other files needed to define the parts that will make up that
shape. For example, the **wing-center** assembly needs a leading-edge,
trailing-edge, and five ribs. All of these files are in the
**wing/wing-center** directory.

While I could have created all of those directories and *scad* files manually, I
wrote a short Python program that generated all of then using an *Excell*
spreadsheet I created as I thought through all of the parts of my design. I
used a basic template file for all of the *scad* files so I would have a start
on the OpenSCAD_ file needed to generate each piece of the design. Most of
these files are pretty short - they simply **use** the needed subassembly *scad*
and position them correctly. The bottom level *scad* files lay out the
individual parts I need to manufacture.

Some manufactured "parts" could actually be constructed out of of of still
smaller parts. For example, some builders construct propeller blades by
laminating several pieces of balsa together. I will not worry about that detail
in this design.

..  note::

    Programmers are a lazy bunch. They would much rather write a program to
    something they could do manually, even if writing that program takes longer
    that doing the job manually. Of course if you intend to do that job more
    than once, you win!

Design Data
===========

We need to define a lot of dimensions and angles in this design. Some of those
dimensions come from the rules, but most come from the design itself.  The data
needed here depends on the part. For spars, for example, we need to define
these dimensions: the length of the spar, and its hight and thickness.

Terms like height, width, and thickness are often used by modelers. I have
tried to use these terms consistently inmy design. *Length always refers to the
long dimension of a part. Thickness refers to the sheet size I will use to cut
the part. *Width* and *height* are measured on the sheet surface when cutting.

..  note::

    Perhaps it would be better to use **x,y**,and **z** for these names, to
    indicate which coordinate direction we mean. However, I am trying to use
    terminology familiar to builders!

Each part will become a single model in OpenSCAD. That part will be
defined in a file containing a module with the part name and any other
supporting modules needed for just that part. General purpose support modules
will be collected in a *utilities* library available to all other code.

Each part can be converted into an **STL** file so that volume, bounding
dimensions, and center-of-gravity estimates can be made. single module so we
can refer to it by name in the code.

The preferred orientation of a part definition in OpensCAD is lying flat on the
X-Y plane, as it would sit on your workbench.



