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
directory, the branches of this tree grow downward in most folks minds to other
directories. The leaves of this tree are the files on your system. You cannot
break things further down.

Directories and files all have names. These names are supposed to be chosen by
you to help you figure out what is being stored in them. A directory groups a
possibly empty set of files and subdirectories. You grouped them for some
reason, so name the directory something nice to help you remember what that
group is about.

Microsoft also decided that names on these directories and files should be able to have spaces in them. That is a nice feature in the office environment, but developers immediately run into problems what names have spaces in them.My afdvice is simple. If ypu stre s developer, asnd you think your nsme should hsv e a spade in it, put an underscore there instead. It will look almost the same whwn you see it on your system, but will cause you far fewer headaches later!@

When building a
project involving computer code, an important decision needs to be made right
at the start.

	How will you manage your code?

Step 1: Create a Project Directory
**********************************

Some developers take a baby step in this direction: they create one project directory and place every project file in this one place. The result over the course of development is *Chaos*!

Why?

Simply because no other developer will be able to figure out what relates to
what. There will always be dependencies in your code: one file needs help from
another file to do its work. Those dependencies are totally invisible to the
reader who is scanning the list of files in your project. I have seen projects
where the main entry point to the program was nearly impossible to locate
without help from magical tools like **grep**, which is sadly missing on PC
systems. (Yet another reason why I ditched my PC and switched to Macs for
development!)

Step 2: Identify Major Components
*********************************

Once you begin serious development of a project, you start to identify the
major components you will build Each one of these components should end up in a
subdirectory of its own. If code in a file in one of your subdirectories needs
nelp from code in another place, that is a *dependency* that you need to
document and implement. The reason for this is simple. Perhaps you are working
on your code and some other developer is working on the code you depend on. If
that other person changes the code you depend on, your code will break. The
only hope is documentation and collaboration to clear up the disconnect.

Sub-Subdirectories
******************

Big components are often broken up still further into smaller components.
Again, create another subdirectory to manage this new smaller component.


u can keep doing this as needed until it make no sense to go further.

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


