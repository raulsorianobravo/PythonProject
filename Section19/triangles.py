#pip install bokeh

#import bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x=[3,7.5,10]
y=[3,6,9]

#prepare the output file

output_file("triangle.html")

#create figure object
f=figure()

#create line plot
f.triangle(x,y,color="#555555",line_width=2)

show(f)