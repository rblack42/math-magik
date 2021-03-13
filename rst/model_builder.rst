ModelBuilder
############

The process of generating a 3D model of a model airplane is a little tedious if done manually. Idecided to generate most of the files needed using a data file written in **json(** a popular data format used in many applications.

The basic scheme will be set up like this:

Root Directory
**************

We will define a toplevel structure that looks like this:

..	code-block:: json

	{
		"LPP": {
		}
	}

The name of the model is specified on this top-level entry, and will become a
directory with the same name.

Inside of that directory, we will create an **scad** file which will be used to
generate the top-level view of the model in OpenSCAD_.

If this file does not exist, the builder will generate one using a **jinja2**
template.

If the file does exist, we will update it to reflect the structure found in the
data file, which we will examine next

Assemblies
**********

The data dictionary found after the model name entry will list the major
assemblies needed to construct the model. The data file will not detail how
this happens, to keep it managable. Instrad, the entries at the next level will
become subdirectories, one for each component needed to build the entity at the
parent level. Each of these directories may end up with subassemblies as well
in a recursive manner. Eventually, we end up with entries that are not
dictionariesm, but simple data items. Those data items will be recorded in the
**scad** file generated for this level.

s an example, the **LPP** model will be constructed using these assemblies:

	* **wing**
	* **stab**
	* **fuselage**
    * **propeller**
	* **wire_parts**

The modifications to the **json** file look like this:

..	code-block:: json

	{
		"LPP": {
			"wing": {
			},
			"stab": {
			},
			"fuselage": {
			},
			"propeller": {
			},
			"wire_parts": {
			}
		}
	}

Generating Modules
******************

As we process the **json** data file we will recursively examine each item
found in the top level dictionary.

The builder will check to see if this entry refers to a dictionary, is is a
simple data item. If this item is a dictionary, a directory eith this name will
be created, if needed, in a development directory. The elements found in the
data file for that item are then scanned, again looking to see if each is a
data item or a dictionary. If the item is adictionar, we will generate a
**use** line for this item, since it will end up a module of its own. If it is
a data item, that item will be collected into a list if data definition lines
that end up in the template. After all items have been examined, the required
module file will be created.

Updating will happen if the module file exists, since that means code might
have been added manually.
