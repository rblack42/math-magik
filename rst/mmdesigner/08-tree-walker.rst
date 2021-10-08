Step 8: Walking the Model Tree
##############################

In thinking through the design of a model using |OSC|, I decided to generate a
directory tree where each level contained at lease one :term:`SCAD` file
defining either a single part to be constructed, or an assembly of parts
producing something like a wing. To make navigating easy, the directory name
will describe the part or assembly, and the :term:`SCAD` file matching the
directory name is the primary design file. Other files may be located next to
this design file, but their names will be unique enough to distinguish then
from a design file. For example, **wing.scad** is a design file located in a
**wing** directory.  **wing_data.scad** is an associated data file, and
**wing_pos.scad** defines data used to position parts that make up the wing.

Once this directory organization structure was set, it became obvious that I
needed a tool that could navigate the directory tree and provide a way to set a
*callback** function in each directory visited.

In this section, we will develop the **TreeWalker** class which will manage
navigating the directory tree and providing a way to activate a *callback*
method to perform some action on files in each directory. This class will need
to provide a way to specify the root directory for a model, the file extension
we are interested in, and the callback method to activate.

Class Constructor
*****************

The class constructor will take a single parameter, which is the root path to
the model we are going to process. The constructor will verify that the
provided path actually points to a directory.

Here is a test that can verify this:
:func:`tests.test_TreeWalker.test_valid_model_path`

Here is the code that confirms we have a valid directory specified for the constructor
model path:

Validating the Model Path
=========================

All valid model directories must have at lease one :term:`SCAD` file, so we
will check that in the constructor. Tests should confirm that passing a model
path that is not a directory, or a directory that contains mo valid
:term:`SCAD` file will be rejected. All methods should return immediately if
the registered model path is None.

Generating File Lists
*********************

The class should provide a **get_file_list** method that returns a list of all
files ending with the registered extension. This list will collect all part and
assembly files. A second method, **get_leaf_file_list**, will return only those
files in leaf directories (containing no subdirectories). These files are the
model parts we need to manufacture to build the model.

Processing Files
****************

Finally, we will provide two routines that actually activate the callback
routines: **process_files** and **process_leaf_files**.
