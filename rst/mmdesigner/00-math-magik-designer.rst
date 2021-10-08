Math Magik Designer
###################

..  warning::

    This project is a work in progress. The application described here is not
    quite ready to use, but that should change soon! You can test the
    installation process now, and update the program when it becomes more
    useful.

The |MM| design application, named |MMD|_ is being developed to assist in the
design of a model using |OSC|_. The application is being written in |PY|_ but
most users will not need to worry about that. Instead, the application will be
distributed as a self-contained package that can be installed like any other
application on your chosen platform. Since most model builders are not
developers, it is likely they use a Windows system, or possible a Mac. Rarely
will they use Linux. In any case, I try to support all three platforms.

..  note::

    Unfortunately, there are many variations of Linux out there, so I will
    limit my testing to just Ubuntu_ which is what I had my students use while
    teaching software develipment!.

This section is intended for model building users of this project. Developers
who might want to contribute to this project will be more interested in the
development notes at :ref:`development-notes`. Those notes walk you through the
complete development of this application.

Getting Started
***************

Assuming you have a suitable computer, which can be running Windows, MacOS, or
Linux, you will need to install just two components:

    * |OSC|_
    * |MMD|


Installing |OSC|
================

Installing |OSC|_ is pretty simple. Navigate to their website at
https://openscad.org/downloads.html and download the installer suitable for your
system. Once it is on your system, run the installer to complete the installation.

Intalling |MMD|
===============

Installing |MMD| is similar. Navigate to
https://www.co-pylit.org/mmdesigner.html and select the version for your
system. Once the file is on your system, run it to complete the installation.

|MMD| User Interface
********************

There are two ways to use this application. One involves typing commands on a
:term:`command line``, and the second uses a traditional mouse-driven approach.

I suspect most modelers are unfamiliar with the :term:`command line`, since it
dates back to the dawn of computing! Developers should be very familiar with
this interface, and it is usually the first interface developed in many
projects. The :term:`command line` is available on all systems:

    * Windows: enter **cmd** in the Windows search box, then click on that program.

    * Mac: Open the **term** application under Applications/Utilities

    * Linux: Open up a new **shell**

On each of these systems, you will see a blank window with some kind of prompt.
This prompt usually tells you where on your computer you are currently working.
At the end of the prompt, you should see some kind of cursor marker indicating
that the system is waiting for you to type in a command. That command will name
some program and let you enter additional parameters that control how the
program will work.

As a simple example, let's check the version of |MMD| currently installed:

..  code-block:: shell

    $ mmd --version


On any of these systems, you can verify that your installation is correct by typing in the following command.
    name authorized to install programs. If you are the owner of the machine, this
is not a problem.

Installing |MMD| is best done using the :term:`command line``. Many modelers may not be familiar with this
 first two are covered in the Appendix
The |MMD| application can be launched as either a
:term:`command line` tool, or as a :term:`graphical user interface` tool.

In this section, we will work through the development of this application. These notes are intended for developers who might wish to contribute to the project. Model builders probably need to refer to the :ref:`users-guide` instead.

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


