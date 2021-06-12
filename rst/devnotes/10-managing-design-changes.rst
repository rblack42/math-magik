Step 10: Managing Design Updates
################################

During the design process, the user's primary focus is on the :term:`SCAD`
files, and supporting data files needed to properly lat out and position every
part in the design. As those :term:`SCAD` files change, various other files
that may have been generated need to be updated as well. How do we make sure
all files are  properly in sync?

The easy way out is to place this burden on the user. They made the change,
they should update the other files. This is easy on the designer, but not the
user.

We can add code that checks the state of the design and triggers an update on
any other files that need to be updated when this code runs. If the user
decides to use to use the :term:`command line interface` the application is
only running during command invocations. So, on program startup, we need to run
the check code before doing anything else.

For the :term:`GUI` interface, the code will be running an event loop, so we
can add code that checks for changes as the user works within the :term:`GUI`.
The Python **watchdog** package could help here, however, that package looks
for file system events, like a save to trigger actions.  That certainly will
work, but not for the :term:`CLI` user.

There is another way to track changes, one used by :program:`git`.

Basic Design File Changes
*************************

If we maintain a hash key for each design file, we can use that code to detect
changes. All we need to do to implement this idea is come up with a place to
store the hash code, and code that checks the design files and verifies that
the hash is different, meaning a change took place. There are not going to be a
large number of such files, so this process can be pretty fast.

Calculating the hash code is simple enough using the :program:`hashlib`
library:

..	code-block:: python

	import hashlib

	def generate_hash(file_name):

	data = '' = 0
	try:
		with open(file_name) as fin:
    		data = fin.read()
	except:  # pragma: no cover
		pass
    hash = hashlib.md5(data).hexdigest()
	return hash

Generating the code is pretty easy, but we need a place to store it.

|OSC| lets you save constant definition data in files with any extension you
like. To make it easier to distinguish design geometry files from data files, I
decided to name all data files with an **.data** extension. When processing
these data items in |PY|, we have another decision to make. We can teach Python
to read the **.data** files, or we can generate the data files from something
more natural for |PY|. My preference is to store data in **.json** files, since
they are very common and easily read and written in python.

Before settling on a scheme, we need to look at the |OSC| data setup.

|OSC| Data Files
****************

The scheme I initially settled on is pretty simple. In each design directory we
will find an :term:`SCAD` file named the same as the directory holding it. This
is the design file for either a part or an assembly. In that same directory, We
will also set up a data file containing any constant data needed by that design
file. Since the current part or assembly may depend on data from a parent
directory (possible more than one level up!) we will **include** the parent
data file in the current data file. If we are consistent doing this, all data
running up the design tree will be available in the current file. This scheme
seemed to work fairly well, until I discovered that the length of the motor
stick depended on an unrelated part, the propeller. If the competition class
limits the total length of the model, we will not know some of the data items
until we figure out the design of the propeller and calculate the geometric
bounds for that assembly!

What this means is that we might need to let the analysis step modify data in
some design files, and iterate the analysis until we have a stable design. This
becomes manageable if we detect design file changes automatically and update the
design, including the basic geometric analysis automatically.

Analysis Data Files
*******************

I decided to store all generated data from the analysis in **.json** files.
These files will include a slot for the material density for part files. The
user will need to enter this data manually, or use the :term:`GUI` interface to
make those changes. If this has not been done when :term:`center of gravity`
calculations are made, the resulting values will be wrong. We will have the
application note that.

To simplify locating these **.json** data files, they will also be named using
the enclosing directory name.


