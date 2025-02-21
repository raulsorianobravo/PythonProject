import justpy as jp

import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as pt

data = pandas.read_csv("./Section21/data/reviews.csv", parse_dates=["Timestamp"])

data["Month"] = data["Timestamp"].dt.strftime('%Y-%m')
month_average_crs = data.groupby(["Month","Course Name"]).mean(numeric_only=True)
month_average_crs = data.groupby(["Month","Course Name"]).mean(numeric_only=True).unstack()


chart_def = """
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Moose and deer hunting in Norway, 2000 - 2024'
    },
    subtitle: {
        text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        // Highlight the last years where moose hunting quickly deminishes
        plotBands: [{
            from: 2020,
            to: 2023,
            color: 'rgba(68, 170, 213, .8)'
        }]
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.3
        }
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766,
                29278,
                27487,
                26007
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048,
                52804,
                49317,
                52490
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

    hc.options.legend.floating = False

    # Problem. Index is not a number of a dot, so 2022-11-1 could be in the graph
    # Must convert the axis
    # hc.options.series[0].data = list(zip(day_avg.index,day_avg["Rating"]))

    hc.options.xAxis.categories = list(month_average_crs.index)
    
    #hc.options.series[0].data = list(month_average_crs["Rating"])

    # Contruct the list
    hc_data = [{"name":v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

    
    hc.options.series = hc_data

    return wp

jp.justpy(appDataFrame, port=8900)