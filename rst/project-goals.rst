Project Goals
#############

This project started off with a few goals in mind.

Visualize the Model
*******************

Most modelers use paper plans to build their design. Those plans are flat and
do not really show you what the model will look like in real life. I started
this project with one simple goal: I wanted to be able to see my design in a
more realistic way. Furthermore, I want to be able to examine it from any angle
I choose, and zoom in to see details. I knew that |OSC|_ could give me that
capability if I could convert my plans into a 3D model.  This was a good
starting point, but I wanted to go further.

Ensure Conformance to Rules
***************************

The designs I plan to come up with will not be of much value for use in
competitions unless they conform to the rules for the chosen competition class.
(Some modelers do not care about the rules, they only fly for fun. That is not
going to be a problem.)

I want my design process to be able to check the rule constraints. By itself,
|OSC|_ cannot help much here. However, it is possible to export your design
into another format more suitable for making calculations that will help.

We will export our design into something called an |STL|_ file (*STL*) format.
We can then create a simple program to process those files to get the data I
need to check conformance with the rules. Since it is relatively simple to
learn, I decided to use |PY|_ as my programming tool.

..	note::

    |PY|_  is simple enough that many kids manage to use it from a very early
    age. It is a very popular first language used in teaching computer
    programming. We will not cover |PY|_ in this work, but I have lecture notes
    for a first course in |PY|_ on my teaching website at
    https://www.co-pylit.org.  I will go over the code I generated for this
    project so you can see how I use it in my analysis of a model design.

Estimate Model Weight
*********************

Indoor modelers sometimes obsess over the weight of things. This is no
surprise. Anything that flies needs to be light, but strong enough to hold
together under the stresses of flight. Lighter airplanes should fly longer than
heavier ones.

Again, STL_ files can be used to give us the weight estimate.

If we identify the density of the material we will use for each part used in
the design, we can add all of those part weights up to get the overall model
weight. I found a nice |PY|_ support package that will process an STL_ file and
give you the total volume of the part defined by that file. If we know the
density of the material we will use when we build that part, we can get an
estimate of the weight.

Unfortunately, estimating the weight of the glue used to bind parts together is
harder to do. Surprisingly, glue weight is a significant contributor to the
final weight of a competition indoor model, so modelers pay attention to this.
To estimate the glue weight, we need to know the surface area of the joints we
will be gluing together and the weight of the glue itself. I have an idea about
doing this which will be included here as I get things worked out.

Locating  Center of Gravity
***************************

We need to locate the center of gravity of our aircraft to ensure it will fly
as desired. This is again something my |PY|_ support code will give us.
Basically, we use the weight and *Center of Mass* location data for each part
in the model to calculate the overall model |CG|.

Perform Aerodynamic Analysis
****************************

I trained as an Aerospace Engineer in college. I almost completed a PhD in that
discipline, but warped into a computer geek instead. I still like to work on
aerodynamics programs, and I would like to do some work on my indoor designs.
However, that part of my goals is not included in this project at the present
time.  Still, having a complete computerized model of my design is a starting
point for further analysis work. Stay tuned to this channel for further
bulletins!

