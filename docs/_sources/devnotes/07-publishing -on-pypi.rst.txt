Step 7: Publishing on PyPi_
###########################

Python packages, including the *mmdesigner* application we are building, usually
end up being published on the |PyPi|_ server. Once there, interested folks can
install this tool on their systems using the standard :command:`pip` command.

Our next job involves adding the structure needed to publish and maintain the
project on PyPi_.

Setup Files
***********

To publish a project on PyPi_, a **setup.py** file is required. This file
contains information about the project that will end up being displayed on
PyPi_ for interested folks to examine. Here is the file for this project:

..  literalinclude::    ../../setup.py
    :linenos:
    :language: python
    :caption: setup.py

Details on all of this can be found in the pyPi_ documentation.

I also added one more file which aids in creating the package uploaded to PyPi_

..  literalinclude::    ../../setup.cfg
    :linenos:
    :language: python
    :caption: setup.cfg

Updating Version Numbers
************************

There is a version number in the **setup.py** file. Every time we create a
version of the project that we want to let users access on PyPi_ we will need
to update this number. PyPi_ does not let you update the version currently
shown (the latest) after publishing it.

So far, the version number appears in three places in this project:

    * README.rst - seen on |GH|

    * mmdesigner/__version__.py - the master project version number

    * setup.py - PyPi_ control file

Managing all three of these can be a problem, so there is a nice tool that helps keep them on track: **bump2version**.

Using this tool, which we can add to the requirements.txt file, involves creating a configuration file that looks like this:

..  literalinclude::    ../../.bumpversion.cfg
    :linenos:
    :language: ini
    :caption: .bumpversion.cfg

..  warning::

    The project is named **bump2version**, but the configuration file is just
    **bumpversion**. The original project developer abandoned the project, and
    a new maintainer renamed it.

With this file n place, we can increment any part of a :term:`semantic versioning` number using one of the new **Makefile** commands provided in the |MMAKE|_ collection:

..  literalinclude::    ../../mk/version.mk
    :linenos:
    :language: make
    :caption: mk/version.mk

Publishing the Project
**********************

Now, when the project reaches a milestone point and you want to release a new version on PyPi_, we need to do a few things:

    * Bump the version number as needed

    * Build the package for PyPi_

    * Test the new version to make sure it will upload properly

    * Publish the version officially

We have already covered the tools needed to bump the version number properly.

Building a Package for PyPi_
============================

To build the package for PyPi_, all we need to do is run the **setup.py** script using |PY|:

..  code-block:: shell

    $ python setup.py sdist bdist_wheel

This command will build two files n a new **dist** directory in the project root directory:

    * mmdesigner-x.x.x-py2.py3-none-any-whl

    * mmdesigner-x.x.x.tar.gz

The first file is the one that will be delivered to a user running the **pip**
command. The second one contains the source code for the project. This is just
the contents of the **mmdesigner** directory, not the full documentation and
test code available on |GH|.

Test The Package for PyPi_
===========================

PyPi_ has a test server that can be used to check the package before it goes
public. We will use the **twine** tool to send this project to the test server:

..  code-block::    shell

    $ twine upload --repository testpypi dist/* --skip-existing

This will upload the new version. If you try to upload an existing version,
nothing will actually be uploaded.

Publish the Package
===================

Finally, we use **twine** to publish the new version officially:

..  code-block:: shell

    $ twine upload  dist/* --skip-existing


All of these commands are included in a |MMAKE|_ module:

..  literalinclude::   ../../mk/pypi.mk
    :language: ini
    :linenos:
    :caption: mk/pypi.mk





