..  _python-setup:

Python Setup
############


In this section, we will go over setting up |PY|_ on your own system.

..  warning::

    There are multiple versions of |PY|_ available. We will be using *Python
    version 3.9* (the latest version) for this project. Many |PY| examples you
    might find on the Internet are designed for the older |PY| 2.7 series. We
    will not be using any of these programs, but beware when you surf for help.

Get the required Resources
##########################

We start off by downloading the installation file we will need. The file can be
obtained from the official |PY|_ project website at http://www.python.org.
(That is where you end up if you click on any of the |PY|_ links). Navigate
to the download page and pick a download that matches your system. For most of
us, we should pick a 64-bit Windows version of Python 3.9.x (where X was 5 when
I did my install).

..  warning::

    You can pick a 32 bit version if you wish, or if your system is an older
    32-bit system.  As of the day I wrote these notes, this is the file I would
    pick:

* `Python 3.9.5 Windows installer <https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe>`_

After the file is on your system,  you can run by double
clicking on the file name in the "Windows Explorer" tool.

..  warning::

    The system will ask you if you want to install this program for a single
    user or all users. Pick all users!

Picking where to install
========================

You can let the program install where Microsoft wants to put things, but as a
person who generates a lot of scripts, I prefer to put my programming tools in
another place.

I set up a directory called ``tools`` at the root of my ``C`` drive. Under that
directory, I place subdirectories for each major tool I install, and I create a
subdirectory named ``bin`` for simple executable tools I install. We will go
over this in the lab. I do this so the ``path`` I need to type into a
:term:`script` will be short and simple.

So, I choose to install |PY|_ in ``c:\tools\Python39`` (no matter what the
last number says).

Setting up the system ``path``
==============================

Before we are ready to run |PY|_, we need to set the system up so it can find
it from the ``command prompt`` we will be using in this project.

To do this. Follow the instructions in the :ref:`command-line` notes and
add ``c:\tools\python39`` to the system ``path variable``. You should also add
``c:\tools\Python39/Scripts`` since we will need it as the course proceeds.

That is all we need to do. To make sure everything works, open up a
``command prompt`` window and type in ``python``. You should see the
interpreter sign on as we did earlier!
