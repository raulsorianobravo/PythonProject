import justpy as jp

import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as pt

data = pandas.read_csv("./Section21/data/reviews.csv", parse_dates=["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime('%Y-%m')

month_average = data.groupby(["Month"]).mean(numeric_only=True)



chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}
"""

#https://quasar.dev/style/typography

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Reviews", classes="text-h1 text-center	")
    p1 = jp.QDiv(a=wp, text = "Graphs of the course")
    hc = jp.HighCharts(a=wp, options= chart_def)

    # Change fields
    #hc.options.title.text = "Title"

    # Change Data
    hc.options.series[0].data = [[3,6], [44,6], [553,0]]

    # or

    x = [3,44,553]
    y = [6,6,1] 
    hc.options.series[0].data = list(zip(x,y))

    return wp

def appDataFrame():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Reviews", classes="text-h1 text-center	")
    p1 = jp.QDiv(a=wp, text = "Graphs of the course")
    hc = jp.HighCharts(a=wp, options= chart_def)

    # Change fields
    #hc.options.title.text = "Title"

    hc.options.title.text = "Ratings by Day"
    hc.options.subtitle.text = "Data provided by the course"

    hc.options.chart.inverted = False
    hc.options.xAxis.title.text = "Date"
    
    hc.options.xAxis.labels.format = "{value}"

    hc.options.yAxis.title.text = "Average Rating"
    hc.options.yAxis.labels.format = "{value}"

    hc.options.series[0].name = "Avg Rating"

    hc.options.tooltip.pointFormat = '{point.x} {point.y}'

    # Problem. Index is not a number of a dot, so 2022-11-1 could be in the graph
    # Must convert the axis
    # hc.options.series[0].data = list(zip(day_avg.index,day_avg["Rating"]))

    hc.options.xAxis.categories = list(month_average.index)
    hc.options.series[0].data = list(month_average["Rating"])

    return wp

jp.justpy(appDataFrame, port=8900)