Introduction
############

In 1955, at the age of nine, I was introduced to the world of model airplanes
by a neighbor who flew a model of the |Gadfly|_ in front of his home.
That fascinating flight marked the start of my career in Aerospace Engineering.
I set out to build and fly my own model airplanes.  Doing so taught me a
lot about the basics of flight.  Eventually, I began building gas-powered
free flight models and entering them in competitions around the East coast.

Then my local club, the Fairfax Model Associates, invited a guest speaker to a
club meeting to speak on building and flying rubber-powered model airplanes
designed to achieve very long flight times in indoor venues. The speaker was
Bill Bigge, an internationally renowned model builder who competed in indoor
rubber-powered events, and was on the U.S. team that went to the Indoor World
Championship event held in Europe. Bill showed off several of his models, and I
was hooked. In fact, Bill became my mentor, and helped me build two airplanes -
well an ornithopter and a helicopter, that I flew to National Record times
while I was still in high school!

I continued building and flying indoor models, and flew them in a variety of
interesting venues, including the TWA hanger at National (now Reagan) Airport
in D.C., a National Guard Armory in Chicago, and the blimp hanger at Lakehurst
Naval Air Station in New Jersey. These model airplanes are extremely light,
very inexpensive to build, and teach you a lot about aeronautical engineering,
which I ended up studying extensively at Virginia Tech.

Then life got in the way. After graduate school, I entered the USAF and started
conducting advanced research in the emerging field of |CFD|_, figuring out
how how air behaves when it flows over an airplane using high-power computers.
I also started flying "real" airplanes (private ones, not Air Force ones). My
model building was put on hold for a long spell.

In 2018, I finally retired after spending 20 years in the USAF, several years
consulting, then a 17 year period teaching Computer Science at Austin Community
College, in Austin, Texas. My wife and I moved to Kansas City to be near family
and I joined the |HAFFA| group. Once again, I was back in the world of model
aviation, and again began building indoor and outdoor rubber-powered airplanes.

Building Plans
**************

Most modelers build their airplanes using paper plans. These plans provide
basic drawings of the model's structure, and the modeler glues up that
structure over those plans using balsa wood and other materials. If you want to
build a large model, the plans get large as well.

Kit Plans
=========

If you purchase a kit, the plans should be included. Often, I decide I may want
to build multiple copies of a model, and building over the plans tends to
destroy them. So I try to get copies of the plan and build on the copy.
Fortunately, my local FedEx_ office has a large-format printer/copier that can
handle that job.

Downloaded Plans
================

There are a lot of sources for plans online, and it is easy enough to download
PDF files which can be printed That is something of a problem for most
builders, since typical home printers cannot produce the plans full size. My
solution has been to take the PDF file to my local FedEx_ office and have them
print out copies for my use. I usually get two, one for reference, and one for
building.

Original Design Plans
=====================

That leaves one category of model left. Suppose you want to build an original
design. Now, we need to generate the plans from scratch. Most model plans are
produced using a *Computer Aided Design* tool. Some of these tools are available
for free, but many modelers use professional CAD programs that are far from
free.  In general all of these programs have a fairly steep learning curve, and
it takes a lot of practice to master well enough to generate the needed plans.
I have used some high-end CAD programs in the past, but I like to focus on
tools that are free, and easy for beginners to use.  (That comes from my
teaching experience!)

3D Modeling
***********

There is one significant problem with the paper plans most modelers use. They
only show flat views of the model, and figuring out how it will look in its
finished form is left to your imagination. For existing designs, construction
articles usually provide pictures of a finished airplane, and some provide
pictures showing how the structure is assembled.

For original designs, you are stuck!

Or are you?

3D Modeling Software
====================

With the explosion of 3D printers, there are new tools designed for 3D modeling
available for our use. Once again, many of these are expensive and complex to
master. What they produce is really fun, though.

A good 3D modeling tool will provide a user interface where you can see the
model as it will look in full 3D form, and spin it around to examine it in
detail. You can zoom in or out to examine the finest details as needed to
verify that the model you have designed is what you want.

Of course, using these tools, you can also generate a 3D print of that model,
but we are not interested in that here - at least for now!

OpenSCAD
========

Some years back, I ran into a 3D modeling tool called OpenSCAD_. This program
is designed for programmers in that you describe your model using code. This is
not like a traditional CAD program that relies heavily on mouse movements to
design things.

Since I am a programmer, and I teach programming to beginners, I really like
generating models with this tool.

Would it be useful in designing model airplanes? Time to find out!

Math Magik
**********

Designing an airplane is an exercise in mathematics. We use a lot of
high-school math in the form of geometry and trigonometry to set things up and
position the parts properly. In designing full-sized airplanes the math gets
much more intense, and working with that math can require very sophisticated
computers. We will not be doing anything in this project that requires more
than a typical home computer.

This project will present a set of 3D models for airplanes that I am currently
building and flying.  The mod eventually els may be designed by others, in
which case i try to derive the model using the original plans, or they may be
of my own design.

Here are the current models to be included in this project:

    * Math-Magik-lpp - a Limited Pennyplane indoor model

    * Slusarczyk-A6 - an A6 class indoor design by Don Slusarczyk

    * Wart - an A-6 class design by HAFFA_ club member Gary Hodson

    * Math-Magik-Sport - a fun-fly rubber powered model suitable for indoor or
      outdoor flying

The rest of the documentation presented here will introduce the basic concepts
needed to understand how we use a tool like OpenSCAD_ to design a model, then we
will work through the design of the *Math Magik lpp* model. Following that, we
will work through the analysis of the design to generate weight and balance
data for the design. In the final section, we will work through the development
of a Python application that can be used to assist in the design and analysis
process.

Hopefully all of this will help others produce nice new designs on their own!
