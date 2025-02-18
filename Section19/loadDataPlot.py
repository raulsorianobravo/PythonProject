#pip install bokeh

#import bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare some data

df = pandas.read_csv("./Section19/data.csv")

x=df["x"]
y=df["y"]

#prepare the output file

output_file("lineFromCsv.html")

#create figure object
f=figure()

#create line plot
f.line(x,y)

show(f)