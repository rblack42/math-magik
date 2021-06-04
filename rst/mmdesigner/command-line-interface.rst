Command Line Interface
######################

The **mmdesigner** program supports a full :term:`command line` interface, and
supports a :term:`graphical user interface` as well. In this section, we will
cover the basic commands supported.

Model Path
**********

Each design managed by **mmdesigner** will be fully contained in a directory
named with the model name. This name may contain spaces, since modelers should
be able to name their models as they see fit.

Inside that model directory, the designer will create a top-level :term:`SCAD`
file, again named with the model name, that assembles the full model. The
existence of this model file will be used to confirm that the directory
contains a model specification.

..	note::

    There can be other :term:`SCAD` files in the model directory, but they will
    be ignored by **mmdesigner**.


Inside the model directory, there will be a system of subdirectories within
this directory defining how the model will be constructed.

The designer should be able to specify a folder where a model will be managed.
The directory containing a model design folder is called the **model_path**

The **mmdesigner** tool will accept a **--path** option that specifies the
location of the parent directory containing the model directory we wish to work
on. A second parameter, **--model** will be used to specify the model name. If
that name contains spaces, it must be enclosed in quotes on the :term:`command
line`.

To simplify things, the user can set an :term:`environment variable`
specifying both of these settings.

    * **MMDESIGNER_PATH** - path to model directories

    * **MMDESIGNER_MODEL** - current working model (below **MMDESIGNER_PATH**)
