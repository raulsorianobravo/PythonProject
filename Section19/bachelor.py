#pip install bokeh

#import bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare some data

df = pandas.read_csv("./Section19/bachelors.csv")

x=df["Year"]
y=df["Engineering"]

#prepare the output file

output_file("Bachelors.html")

#create figure object
f=figure()

#create line plot
f.line(x,y)

show(f)