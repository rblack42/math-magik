Testing Setup
#############

This project used |TDD|, a development process designed to create more reliable
programs.

Basically this process involves thinking up a new feature you want to add to
the project, then asking yourself how you will know that new feature works. You
write test code that check to see if the feature works properly. The tests are
used to gauge if work on the feature is done. You run the tests and make
changes until they work. In fact, you continue to run those tests as you make
further changes to the project, adding yet more features. This process ensures
that new features do not break old features.

Once this process is set up, you cam even run these tests on multiple platforms
using on of the popular |CI| services available today. I will be using |GH|
"Workflows" to test this project on Mac, Widows, and Linux systems. I will also
use Travis-CI_ to do similar tests, and AppVeyor_ to test in Windows.

Using multiple services helps generate confidence that your project is really
ready for use when you publish releases of the project for the public.


