Step 4: Continuous Integration
##############################

Many program development projects (most?) rely on |CI| to ensure their code is
always ready for deployment on a number of platforms.

For |OS| developers, there are a number of free |CI| services that can be used
to test projects on a number of different platforms.

This project will use three services for |CI| testing:

    * |GH|_

    * Travis-CI_

    * AppVeyor_

In this section, we will configure all three services for basic project testing.

GitHub Workflows
****************

Hosting your project on |GH| provides an easy way to test your code.  Setting
up a basic test process is as easy as clicking on :menuselection:`Actions` then
scrolling down until you see the :menuselection:`Python application` entry.
Selecting this will create a new directory in your project named **.github**.
Under a **workflows** subdirectory you will find a file named
**python_app.yml**. This is a :term:`YAML` file contsaining instructions on how
to clone your project into a :term:`virtual machine`, install any dependencies,
then run tests on your code.

..  literalinclude::    ../../.github/workflows/python-app.yml
    :language: yaml
    :linenos:


Travis-CI
*********

Setting up testing on Travis-CI_ is similar. We need to create another control
file, this one named **.travis.yml**. This needs to be placed in the root
directory of the project. For this initial example, we will again test on a
Linux host.

..  literalinclude::    ../../.travis.yml
    :linenos:
    :language: yaml

To activate testing, you need to set up an account on Travis-CI_, which can be
done using your username and password from |GH|. Once that has been done, log
in and you click on :menuselection:`Settings`. On this page you will see a
:menuselection:`Sync account` button that will make sure you see all
repositories you have on |GH| (I have over 100!). Scroll down until you see the
project you are working on and click on the :menuselection:`Setting button on
the right side of the repository name. In the next panel, make sure both the
:menuselection:`Build pushed branches` and :menuselection:`Build pushed pull
requests` are selected.

Now, navigate to your |GH| account and click on your account image. Select
:menuselection:`Settings --> Applications`. You need to grant Travis-CI_ access
to your account so it can receive notifications every time you push new changes
to |GH|. When that happens, Travis-CI_ will create a new :term:`virtual
machine`, clone your updated code, and run the tests specified in the control
file.

As with |GH|, we can add a badge to the **README.rst** file showing the results.
