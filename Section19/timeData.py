from bokeh.plotting import figure, output_file, show
import pandas

df= pandas.read_csv("./Section19/adbe.csv", parse_dates=["Date"])

p=figure(width=1500,height=500, x_axis_type="datetime")

p.line(df["Date"],df["Close"], color="red", alpha=0.5)

output_file("Timeseries.html")


p.title.text = "Data"
p.title.text_color = "Orange"
p.title.text_font = "times"
p.title.text_font_style = "italic"
p.yaxis.minor_tick_line_color = "Yellow"
p.xaxis.axis_label = "Times"
p.yaxis.axis_label = "Value"

show(p)