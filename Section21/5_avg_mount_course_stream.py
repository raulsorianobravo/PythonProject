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
    type: 'streamgraph',
    marginBottom: 30,
    zooming: {
      type: 'x'
    }
  },

  // Make sure connected countries have similar colors
  

  title: {
    floating: true,
    align: 'left',
    text: 'Winter Olympic Medal Wins'
  },
  subtitle: {
    floating: true,
    align: 'left',
    y: 30,
    text: 'Source: <a href="https://www.olympedia.org/statistics">olympedia.org</a>'
  },

  xAxis: {
    maxPadding: 0,
    type: 'category',
    crosshair: true,
    categories: [
    ],
    labels: {
      align: 'left',
      reserveSpace: false,
      rotation: 270
    },
    lineWidth: 0,
    margin: 20,
    tickWidth: 0
  },

  yAxis: {
    visible: false,
    startOnTick: false,
    endOnTick: false,
    minPadding: 0.1,
    maxPadding: 0.15
  },

  legend: {
    enabled: false
  },

  annotations: [{
    labels: [{
      point: {
        x: 5.5,
        xAxis: 0,
        y: 30,
        yAxis: 0
      },
      text: 'Course Launched'
    }, {
      point: {
        x: 18,
        xAxis: 0,
        y: 90,
        yAxis: 0
      },
      text: 'Python got popular'
    }],
    labelOptions: {
      backgroundColor: 'rgba(255,255,255,0.5)',
      borderColor: 'silver'
    }
  }],

  plotOptions: {
    series: {
      label: {
        minFontSize: 5,
        maxFontSize: 15,
        style: {
          color: 'rgba(255,255,255,0.75)'
        }
      },
      accessibility: {
        exposeAsGroupOnly: true
      }
    }
  },

  // Data parsed with olympic-medals.node.js
  series: [{
    name: 'Finland',
    data: [
      0, 11, 4, 3, 6, 0, 0, 6, 9, 7, 8, 10, 5, 5, 7, 9, 13, 7,
      7, 6, 12, 7, 9, 5, 5, 6, 8
    ]
  }, {
    name: 'Austria',
    data: [
      0, 3, 4, 2, 4, 0, 0, 8, 8, 11, 6, 12, 11, 5, 6, 7, 1, 10,
      21, 9, 17, 17, 23, 16, 17, 14, 18
    ]
  }, {
    name: 'Sweden',
    data: [
      0, 2, 5, 3, 7, 0, 0, 10, 4, 10, 7, 7, 8, 4, 2, 4, 8, 6, 4,
      3, 3, 7, 14, 11, 15, 14, 18
    ]
  }, {
    name: 'Norway',
    data: [
      0, 17, 15, 10, 15, 0, 0, 10, 16, 4, 6, 15, 14, 12, 7, 10,
      9, 5, 20, 26, 25, 25, 19, 23, 26, 39, 37
    ]
  }, {
    name: 'U.S.',
    data: [
      0, 4, 6, 12, 4, 0, 0, 9, 11, 7, 10, 7, 7, 8, 10, 12, 8, 6,
      11, 13, 13, 34, 25, 37, 28, 23, 25
    ]
  }, {
    name: 'East Germany',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 14, 19, 23, 24, 25,
      0, 0, 0, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: 'West Germany',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 5, 10, 5, 4, 8, 0,
      0, 0, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: 'Germany',
    data: [
      0, 0, 1, 2, 6, 0, 0, 0, 7, 2, 8, 9, 0, 0, 0, 0, 0, 0, 26,
      24, 29, 36, 29, 30, 19, 31, 27
    ]
  }, {
    name: 'Netherlands',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 2, 9, 9, 6, 4, 0, 7, 4,
      4, 11, 8, 9, 8, 24, 20, 17
    ]
  }, {
    name: 'Italy',
    data: [
      0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 1, 4, 4, 5, 4, 2, 2, 5, 14,
      20, 10, 13, 11, 5, 8, 10, 17
    ]
  }, {
    name: 'Canada',
    data: [
      0, 1, 1, 7, 1, 0, 0, 3, 2, 3, 4, 3, 3, 1, 3, 2, 4, 5, 7,
      13, 15, 17, 24, 26, 25, 29, 26
    ]
  }, {
    name: 'Switzerland',
    data: [
      0, 3, 1, 1, 3, 0, 0, 10, 2, 6, 2, 0, 6, 10, 5, 5, 5, 15,
      3, 9, 7, 11, 14, 9, 11, 15, 15
    ]
  }, {
    name: 'Great Britain',
    data: [
      0, 4, 1, 0, 3, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0,
      2, 1, 2, 1, 1, 4, 5, 2
    ]
  }, {
    name: 'France',
    data: [
      0, 3, 1, 1, 1, 0, 0, 5, 1, 0, 3, 7, 9, 3, 1, 1, 3, 2, 9,
      5, 8, 11, 9, 11, 15, 15, 14
    ]
  }, {
    name: 'Hungary',
    data: [
      0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 1, 3
    ]
  }, {
    name: 'Soviet Union',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 21, 25, 13, 16, 27, 22, 25,
      29, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: 'Unified Team',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23,
      0, 0, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: 'Russia',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      23, 18, 13, 22, 15, 33, 0, 0
    ]
  }, {
    name: 'ROC',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 17, 32
    ]
  }, {
    name: 'Japan',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 1, 1, 1, 7,
      5, 10, 2, 1, 5, 8, 13, 18
    ]
  }, {
    name: 'Czechoslovakia',
    data: [
      0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 4, 3, 1, 1, 6, 3, 3,
      0, 0, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: 'Poland',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0,
      0, 0, 2, 2, 6, 6, 2, 1
    ]
  }, {
    name: 'Spain',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
      0, 0, 0, 0, 0, 0, 2, 1
    ]
  }, {
    name: 'China',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3,
      3, 8, 8, 11, 11, 9, 9, 15
    ]
  }, {
    name: 'South Korea',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4,
      6, 6, 4, 11, 14, 8, 17, 9
    ]
  }, {
    name: 'Czech Republic',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 3, 3, 4, 6, 8, 7, 2
    ]
  }, {
    name: 'Belarus',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      2, 2, 1, 1, 3, 6, 3, 2
    ]
  }, {
    name: 'Kazakhstan',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      3, 2, 0, 0, 1, 1, 1, 0
    ]
  }, {
    name: 'Bulgaria',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
      0, 1, 3, 1, 0, 0, 0, 0
    ]
  }, {
    name: 'Denmark',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 1, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: 'Ukraine',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      2, 1, 0, 2, 0, 2, 1, 1
    ]
  }, {
    name: 'Australia',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      1, 1, 2, 2, 3, 3, 3, 4
    ]
  }, {
    name: 'Belgium',
    data: [
      0, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 1, 0, 0, 0, 0, 1, 2
    ]
  }, {
    name: 'Romania',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: 'Liechtenstein',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 2, 1, 0,
      0, 0, 0, 0, 0, 0, 1, 0
    ]
  }, {
    name: 'Yugoslavia',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0,
      0, 0, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: 'Luxembourg',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
      0, 0, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: 'New Zealand',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
      0, 0, 0, 0, 0, 0, 2, 3
    ]
  }, {
    name: 'North Korea',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
      0, 0, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: 'Slovakia',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 1, 3, 1, 3, 2
    ]
  }, {
    name: 'Croatia',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 4, 3, 3, 1, 0, 0
    ]
  }, {
    name: 'Slovenia',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      3, 0, 1, 0, 3, 8, 2, 7
    ]
  }, {
    name: 'Latvia',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 1, 2, 4, 1, 1
    ]
  }, {
    name: 'Estonia',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 3, 3, 1, 0, 0, 1
    ]
  }, {
    name: 'Uzbekistan',
    data: [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      1, 0, 0, 0, 0, 0, 0, 0
    ]
  }],

  exporting: {
    sourceWidth: 800,
    sourceHeight: 600
  }

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