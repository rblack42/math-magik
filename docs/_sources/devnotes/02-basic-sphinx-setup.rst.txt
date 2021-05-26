Step 2: Basic Sphinx Setup
##########################

All projects should be documented. I am not talking about sprinkling code with
comments, that is not documentation. A well documented project has material
aimed at the users of the product, and the developers of the project. The users
obviously need to know how to use the product, and developers need to know how and why it
was put together the way it is presented. Those developers may need to fix
bugs in the project, or add new features. The developers may not even have been
part of the original team that put the project together.

Sadly, many projects fail to address these documentation needs.

The |PY| world has settled on a nice documentation tool called Sphinx_. This
tool processes simple text documents written in a simple markup language called
|RST|, that is quite readable even without processing. The Sphinx_ tool can
generate many different types of output, but we will focus only on two:
:term:`HTML` for display on the web, and :term:`LaTeX` which can be used to
generate :term:`PDF` output.

Installing Sphinx_
******************

Since Sphinx_ is a |PY| tool, installation is accomplished using the standard
:command"`pip` tool. This can be run from a :term:`command line`, but since I
am going to develop this project using PyCharm_ we will install it inside the
:term:`IDE`:

Start up PyCharm and open the project. Then select :menuselection:`PyCharm -->
Preferences` Next select :menuselection:`Project: math-magik --> Python
Interpreter`. Click on the :menuselection:`gear` icon at the right side of the
selection window. This window will create a Python *virtual environent` where
all project dependencies will be manages separated from any other |PY| projects
you might be working on. The default **venv** directory will be initialized
with a |PY| interpreter and all packages needed for the project will be
installed inside this directory as well.

Click :menuselection:`OK` when you are satisfied with the entries. Once the
**venv** directory has been set up make sure that the |PY| interpreter points
to  **venv/bin/python**.

Next, create a new **requirements.txt** file in the top level project
directory. Open this file and add this line:

..	code-block:: text

	sphinx

Once that line is in place, select :menuselection:`Install requirement` and the
:term:`IDE` will install Sphinx_.

..	note::


    All future project requirements will be lsted in this file and installed
    the same way.

Set up a Sphinx_ Project
************************

We will be publishing the documentation for this project using |GH| *Pages*, a
free hosting service to |GH| users. All :term:`HTML` web pages stored in a
**docs** directory in the project will be made visible after we do a little
setup work on |GH|.

Start off by creating two directories: **docs** and **rst**. We will create our
documentation source files under the **rst** directory and generate web pages
in the **docs** directory. Both of these directories can be created using the
:menuselection:`File --> New --> Directory` menu.

RUn **Sphinx Quickstart**
*************************

Select :menuselection:`Tools --> Run Sphinx Quickstart`. Change the path shown
so it points to the **rst** directory, then click :menuselection:`OK`.

In the console panel you will be asked a few questions. Just press :kbd``Enter`
except for these entries:

	* Author - Add your name

	* Project Release - Most projects start off with release 0.1.0

This step creates several files in the **rst** directory.

You should check the **conf.py** file to make sure your setting are correct.

Create a Documentation Run Configuration
****************************************

Select :menuselection:`Run --> Edit Configurations`. Click on
:menuselection:`Add new configuration --> Sphinx Task`. Make sure the **Input**
field points to the **rst** directory and the **Output** field points to the
**docs** directory. When you are ready, click on :menuselection:`OK`.

Test Build
**********

Now you can test the documentation setup by selecting :menuselection:`Run -->
Sphinx Task`. With any luck, your first documentation build will appear in the
**docs** folder.

Push to |GH|
************

We can now push the changes to the project to |GH|. Unfortunately, doing
everything needed for this step inside PyCharm_ proved impossible. PyCharm had
already added both its special **.idea** directory and the 88venv** directory,
both of which I did not want posted on |GH|. The fix was to open up a
:term:`command line` and do these commands:

..	code-block:: shell

	$ git reset .idea
	$ git reset venv
	$ git status
	$ git add .
	$ git status
	$ git commit -m "Initial Sphinx setup"
	$ git push

At this point, navigate to your project on |GH| and select
:menuselection:`Settings`. Scroll down to the **Github Pages** area.
Make sure the branch is **main** and the **docs** folder is selected. Once
these are set click on :menuselection:`Save`. You can now navigate to the
public pages:

..	code-block:: text

	https://rblack42.github.io/math-magik


Adding a Custom Theme
*********************

By default, Sphinx_ uses a pretty bland theme. I looked at several themes on
the Internet and discovered that I looked to one Sphinx_ uses on its own
project pages! So, I copied that theme into this project The additions are now
in the project directory and changes to the **conf.py** file are in place as
well.

..	todo::

    Add documentation on customizing this theme.
