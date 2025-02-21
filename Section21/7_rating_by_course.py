import justpy as jp

import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as pt

data = pandas.read_csv("./Section21/data/reviews.csv", parse_dates=["Timestamp"])

# data["Weekday"] = data["Timestamp"].dt.strftime('%A')
# data["Weekdaynumber"] = data["Timestamp"].dt.strftime('%w')

share = data.groupby(["Course Name"])["Rating"].count()



chart_def = """
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Egg Yolk Composition'
    },
    tooltip: {
        valueSuffix: '%'
    },
    subtitle: {
        text:
        'Source:<a href="https://www.mdpi.com/2072-6643/11/3/684/htm" target="_default">MDPI</a>'
    },
    plotOptions: {
        series: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: [{
                enabled: true,
                distance: 20
            }, {
                enabled: true,
                distance: -40,
                format: '{point.percentage:.1f}%',
                style: {
                    fontSize: '1.2em',
                    textOutline: 'none',
                    opacity: 0.7
                },
                filter: {
                    operator: '>',
                    property: 'percentage',
                    value: 10
                }
            }]
        }
    },
    series: [
        {
            name: 'Percentage',
            colorByPoint: true,
            data: [
                {
                    name: 'Water',
                    y: 55.02
                },
                {
                    name: 'Fat',
                    sliced: true,
                    selected: true,
                    y: 26.71
                },
                {
                    name: 'Carbohydrates',
                    y: 1.09
                },
                {
                    name: 'Protein',
                    y: 15.5
                },
                {
                    name: 'Ash',
                    y: 1.68
                }
            ]
        }
    ]
}
"""


#https://quasar.dev/style/typography



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

    hc.options.legend.floating = False

    # Problem. Index is not a number of a dot, so 2022-11-1 could be in the graph
    # Must convert the axis
    # hc.options.series[0].data = list(zip(day_avg.index,day_avg["Rating"]))

    hc.options.xAxis.categories = list(share.index.get_level_values(0)) 
    

    # Contruct the list
    hc_data = [{"name":v1, "y":v2} for v1, v2 in zip(share.index, share)]
 
    hc.options.series[0].data = hc_data

    return wp

jp.justpy(appDataFrame, port=8900)