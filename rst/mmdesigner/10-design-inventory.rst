Design Inventory
################

It is nice to be able to see a basic inventory of the components in your
design. Generating such an inventory seems simple enough: scan the entire
design directory tree and count the files found. The problem we face in this
task is looking at each directory and file and figuring out what that
contributes to the inventory. 

Basically, we will want t count the following items:

	* Parts - a directory with no subdirectories i=hold a part
	* Assemblies - a directory with subdirectories holds an assembly
	* Data Files: files that end with **_data.scad**
	* Position data files - files that end with with **_pos.scad**
	* STL files - files that end with **.stl**
	* Mass property files - files that end with **.json**


