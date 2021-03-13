Weight and Balance Calculations
###############################

OpenSCAD_ and a Python_ library called **mimpy-stl** will let us generate the
volume of a model, and locate the center of gravity. That is a pretty cool
capability, and one we can use to get an estimate of the flying weight of a
proposed model, and locate the predicted COG>

However, this package was designed for 3D printing, and therefore assumes that
the entire model is going to be made of one material with a consistent density.
That is definitely not the case for model airplanes., especially those intended
for competition!

Most indoor model builders choose the density they feel is appropriate for
every piece of their model. The final weight and center of gravity location
therefore depends on those density decisions.

If we try to apply the libraries analysis tools on the completed model, we will not
get accurate results. Instead, we need ot perform an analysis on each distinct
piece of the model, then run a calculation to get the final weight and balance
data. Fortunately, this is not that hard.

Analyze each part individually.

To use these tool for our analysis, we will create a file that generates each
physical part you would construct in building your model. The final placement
of that part needs to be established for accurate center of gravity
calculations. For the weight assessment, we could just get the volume of each
part and multiply that by the selected density for that part.

For COG calculations, the position is needed. The library will locate the
center of mass for the part, which we will combine with position data to perform
the COG assessment.

Designing for Analysis
**********************

My goal is to automate the analysis and generate a detailed report of the
results. To do this, each distinct part will end up in one file located in the
design directory system. Although we could process a design with multiple parts
in a single file, we still need to get OpenSCAD to export an **STL** file for
each part so the Python library can do its work. In the end, it is just easier
to manage things when each part is in own own file.


