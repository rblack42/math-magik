Math Magik Designer CLI
#######################

The |MM| design application, named **mmd**, can be launched as either a
:term:`command line` tool, or as a :term:`graphical user interface` tool.

..	note::

	The :term:`GUI` version is undergoing development at present.

Command Line Interface
**********************

In this section, we will show the **mmd** application can be used in your model design work.

First, just typing **mmd** on the :term:`command line` will display a help
message to show you all available commands and options that can be used.

..	command-output::	mmd

You can also ask for help explicitly"

..	command-output::	mmd --help

Unfortunately, this help message does not show you everything about possible
commands. The list of commands shown have additional parameters you can see by
asking for help on them:

..  command-output::    mmd stl --help

Here the **-all** parameter will attempt to do a :term:`STL` files for the
entire design. (This can take a while!)


