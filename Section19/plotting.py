from motionGraph import df
from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type='datetime', height=800, width=1000, title="Motion Graph")

p.yaxis.minor_tick_line_color=None
p.yaxis.ticker.desired_num_ticks=1

q = p.quad(left=df["Start"] , right=df["End"], bottom=0, top=1, color="green")

output_file("Graph.html")
show(p)