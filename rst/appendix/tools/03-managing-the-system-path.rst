Configuring the PATH on Windows 10
##################################

When you work on the command line, you will name a program as part of the
command, then provide additional parameters needed by that program on the rest
of the line. The command line is just a space separated list of text parts,
most of which are available to the program to process as it sees fit.

Sure, some of you launch programs by clicking on icons. In that case, Windows
uses information recorded with that icon to figure out how to launch your
program and provide options.

The tricky part is making sure the operating system can actually find the
program file.

The System PATH
***************

Windows maintains a list of places to look for programs. That list is recorded
in something called the "System PATH Environment Variable". We can get a look
at that list by doing this:

..	code-block:: bash

	> set path
	Path=C:\Program Files;C:\Python39; ...

This list can be pretty long.

Windows 10 has an interesting tool called "where" to locate files. It really is
not useful for finding things in general, but we can check the Python
executable here:

..	code-block:: bash

	> where python.*
	C:\Python39\python.exe

When I look for my favorite programmer's editor ``gvim``, this is what I see:

..	code-block:: bash

	> where gvim.*
	C:\Windows\gvim.bat

A "batch" file (ending with ``.bat``) is a script Windows uses to manage things.
In this case, the ``gvim`` installer added this file for me when I told it I
wanted to run `vim`` from the command line.

We will not look at that file here. Instead, we want to see how to make Windows
find our program files, even if the installer failed to set things up
correctly.

Step 1: Find your Executable
****************************

This is actually harder than it should be on Windows. When you install any
program, you have some say where things will land, but many beginners miss
that. Now, you have to hunt for your program. Most of the time the program will
end up under ``C:\Program Files`` or ``C:\Program Files (x86)``. You will
probably find the executable file in a subdirectory under one of those places.
The directory name will give you a clue. For example, Git is installed in
``C:\Program Files\Git\cmd``. The actual program name will end with ``.exe``.
For git the file is named ``git.exe``.

Once you have located your program, write down the path to the directory where
that executable file lives.

For Git_, this would be ``C:\Program Files\Git\cmd``

Step 2: Open Up the PATH Edit Tool
**********************************

Once you know where your program lives, type "system properties" in the Windows
search box at the bottom left of the screen.

Next, click on "System Info" in the "Related Settings" section.

Now, click on "Advanced system settings" (Phew!)

Click on the "Environment Variables" button at the bottom of this page.

In the bottom panel, labeled "System variables", scroll down until you see an
entry named "Path". Select that line, then click on the "Edit" button.

In the edit panel that opens up, click on "New", and type in the path you
identified earlier. On most of my systems, I put simple executable files in
``C:\tools\bin``, so that is what I would type in to make sure these simple
programs can tun from the command line.

You can add several new places to look here. Just click on "New" each time.

When you are done, Click on "OK", them close all the windows you have left
open.

Step 3: Open a New Command Prompt
*********************************

Windows loads all of this PATH information when it first opens up a command
prompt window. Any such windows you have open at this point will not see your
new PATH settings. Close them, then reopen them. Now try to start your program.
If it still does not work, try that "where" tool, and if that fails, try
editing the PATH variable again, you may have made a typing mistake!

