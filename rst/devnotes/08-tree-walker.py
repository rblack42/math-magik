Step 8: Walking the Model Tree
##############################

In thinking through the design of a model using |OSC|, I decided to generate a
directory tree where each level contained at lease one ;term:`SCAD` file
defining either a single part to be constructed, or an assembly of parts to be
combined into something like a wing. Once that decision had been made the need
to a routine that can "walk' this design tree and process files became obvious.

in this section, we will develop the **TreeWalker** class which will manage
navigating the directory tree and providing a way to activate a *callback*
method to perform some action on files in each directory. This class will need
to provide a way to specify the root directory for a model, the rile extension
we are interested in and the callback method to activate.

Class Constructor
*****************

The class constructor will take a single parameter, which is the root path to
the model we are going to process. To make sure we actually point to a model
directory, we will require that the specified directory contain at least on
:term:`SCAD` file

Here is a test that can verify this:

..  literalinclude::    ../../tests/test_model_path.py
    :caption: tests/test-model-path.py
    :linenos:
    :language: python

