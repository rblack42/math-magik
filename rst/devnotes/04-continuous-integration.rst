Continuous Integration
######################

Many program development projects (most?) rely on |CI| to ensure their code is
always ready for deployment on a number of platforms.

For |OS| developers, there are a number of free |CI| services that can be used
to test projects on a number of different platforms.

This project will use three services for |CI| testing:

    * GitHub_

    * Travis_CI_

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

..  literalinclude::    ../../.github/worlflow/python_app.yml
    :linenos:


