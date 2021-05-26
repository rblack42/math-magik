Step 1: Create |GH|_ Repo
#########################

To start a new project, in this case a |PY|_ project, we need to create a home
for the code on |GH|_. All programming projects should be managed using some for
of control system. Today, the most popular system is Git_, developed by `Linus
Torvalds`_ of Linux fame. For projects managed using Git_ |GH| is probably the
most popular site to host your |OS| code. (So popular that Microsoft bought
|GH| a few years ago!)

Create a |GH| Account
*********************

|GH| is a free service for most folks. They do offer paid services, but those
are not important in this project.

Navigate to their website and click on the :menuselection:`sign up` button on
the page. You will need to come up with a suitable user name (mine is **rblack42**)
and provide a password and a valid ema1l address. Once your account is active,
you will have a home page on |GH| that you can reach by navigating to |GH| like
so:

..	code-block:: text

	https://githib.com/rblack42

You will need to provide your credentials to gain access, but you can add a
public key to your account and set up things to allow immediate access. This is
very handy. See :ref:`github-setup` for more information.


You can edit your public profile to provide an image of you and other
information folks browsing your site may find interesting. |GH| is a great
place to show off your skills and interests.


Create the Project Repository
*****************************

Navigate to your |GH| home page. Click on your account icon at the top right of
the window. Select :menuselection:`Your Repositories`, then click on the
:menuselection:`New` button. You need to come up with a project name. For this
project, I am using **math-magik**. I add a suitable License to the project but
I do not add anything else at this point. I will configure things
later.

Workstation setup
*****************

Before you proceed further in this project, you need to get a few tools installed on your development machine. Basically we will be using these tools for this project:

    * |PY|_ - Needed for documentation and the project application

    * PyCharm_ - a free |PY| :term:`Integrated Develpment Environment` (:term:`IDE`)

    * Git_ _ for source code management

I like to use the :term:`command line` for some things, but for this project, I will focus on using PyCharm_ as much as possible.

Details on installing these tools on your machine ae included in the Appendix (:ref:`tool-setup`)

Clone this Repo
***************

Once the basic repository is in place on |GH|, we need to "clone" it on our
local workstation to start development work. I keep all of my active development
projects in a directory named **_dev** on my development machine (I use a
Macbook Pro).
This sets up a new directory in **_dev** with the project name. This is a git-
repository already ready to post changes to the project back up to the |GH|_
server.

..	note::

    if you qre a developer and wish to contribute to the |MM| project, please
    follow the instructions at :ref:develop to get properly set up. If you
    "clone" the main project directly, you will not be able to post your
    changes in a way I can use.


