Model Directory Structure
#########################

Let's get one thing straight now. I am going to discuss directories you use to
manage your project. If you have worked on PCs long enough, you know that
Microsoft decided we should call these things "folders", in keeping with their
goal of making computer management feel like something you do in your office.
You know, you manage pieces of paper you put in "folders", then stuff them away
in filing cabinets. I have always wondered why they did not decide we should
call our hard disks "cabinets" Oh well!

What is a Directory?
********************

A directory is a management structure on your systems hard disk that helps you
organize (and find) things. You can place "files" in a directory, or other
sub-directories. It really does not matter how a directory is actually set up
on your system. Instead, what matters is how you "think" about things on your
system. Microsoft wanted you to think like you do when working in an office
environment using a computer (running Windows, of course).

    Hmmm! Wonder where the term "windows" came from. Maybe some developer was
    staring out the office window trying to come up with a name!

Files can be programs, data, or just documents. In general, these things are
not to be broken up onto smaller pieces. You would never tear a report apart and put
the individual pages in separate folders, would you?

Files are processed by some program on your system, like Word, or launched by
your operating system when you double-click your mouse on some icon.

Subdirectories
===============

Directories can also contain other directories. We call these inner directories
"subdirectories". These subdirectories can contain more files, or more
subdirectories, leading to a tree-like system (Ok, an upside down tree) of
directories and subdirectories. The "root" of this tree is the top-most
directory, the branches of this tree grow downward, in most folks minds, to other
directories. The leaves of this tree are the files on your system. You cannot
break those things further down.

Directories and files all have names. These names are supposed to be chosen by
you to help you figure out what is being stored in them. A directory groups a
possibly empty set of files and subdirectories. You grouped them for some
reason, so name the directory something nice to help you remember what that
group is about.

Microsoft also decided that names on these directories and files should be able
to have spaces in them. That is a nice feature in the office environment, but
developers immediately run into problems when names have spaces in them. My
advice is simple. If you are a developer, and you think your name should have
a space in it, put an underscore there instead. It will look almost the same
when you see it on your system, but will cause you far fewer headaches later!

Organizing Program Code
***********************

When building a project involving computer code, an important decision needs to
be made right at the start.

	How will you manage your code?

Step 1: Create a Project Directory
**********************************

Some developers take a baby step in this direction: they create one directory
and place every project file they create in this one place. The result over the
course of development is *Chaos*!

Why?

Simply because no other developer will be able to figure out what relates to
what. There will always be dependencies in your code: one file needs help from
another file to do its work. Those dependencies are totally invisible to the
reader who is scanning the list of files in your project. I have seen projects
where the main entry point to the program was nearly impossible to locate
without help from magical tools like **grep** which can locate strings inside
of files. Sadly, this tool is missing on PC systems. (Yet another reason why I
ditched my PC and switched to Macs for development!)

Step 2: Identify Major Components
*********************************

Once you begin serious development of a project, you start to identify the
major components you will build. Each one of these components should end up in a
subdirectory of its own. If code in a file in one of your subdirectories needs
help from code in another place, that is a *dependency* that you need to
document and implement. The reason for this is simple. Perhaps you are working
on your code and some other developer is working on the code you depend on. If
that other person changes the code you depend on, your code will break. The
only hope is documentation and collaboration to clear up the disconnect.

Sub-Subdirectories
******************

Big components are often broken up still further into smaller components.
Again, create another subdirectory to manage this new smaller component.


You can keep doing this as needed until it make no sense to go further.

Directory Trees
***************

The result of all this decomposing a large project into a bunch of smaller
projects is a structure we call a "directory tree". The "root" of this tree is
the top-most project directory. The branches lead to subdirectories off of the
root, further branches take us to lower level subdirectories, and so on until
we reach the leaves of this tree which are the files we really want to work on.

There are nice tools available that will show you this tree for your project.
For example, for my *Limited Pennyplane** project, here is the tree showing the
**scad** files in the project, produced on my Mac using such a tool oddly
enough called **tree**.:

..  literaninclude::    files/MMtree.txt
    :linenos

That is a lot of files and directories!

|OSC|_ lets you **include** another file, which has the effect of copying that
included file into the current file at the point where the **include** line is
located. It also lets you *use* another file, which provides access to those
*modules* we mentioned earlier from the *used* file. This allows you to *call*
modules to do some work in the first file.  We will see a lot of this kind of
code as we work through the design!

In setting up this project, I decided to create four kinds of **scad** files:

    * Basic part file - **include** only data files, may **use** library files

    * assembly files - **include** data and position files, **use** part or
      assembly files

    * Data files - define various values used to size and position things, may
      **include** other data files

    * Position files - used to properly position parts or assemblies.
      **include** data files only

I also set up a naming convention to keep track of what is in each file:

    * part or assembly - named to identify the component

    * Data file - ends in **_data.scad**

    * Position file - ends with **_pos.scad**

This ended up generating a lot of files, and a future modification of this
project may merge some of these.

The important point to make here is that this directory structure allows
repeated use of common part names. For instance, both the wing and stabilizer
have leading edge parts, and making the names for these parts unique would make
them longer than needed. In fact, I use a common abbreviation ***le** for each
one, located in a **wing** or **stab** subdirectory.

Notice also that the leading edge part is managed in a directory with the same
name. This allows generated files from the analysis process we have not
discussed yet to be stored with the associated part.

I created this directory structure as I created each component for the design.
My plan is to have the design application that is part of this project help
manage this process.

With this background, we can now start the actual design process. But before
diving deep into that, we need to talk a bit about how you actually write and
debug |OSC|_ code, That comes next!

