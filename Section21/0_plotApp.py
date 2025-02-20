
# pip install justpy

import justpy as jp


#https://quasar.dev/style/typography

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Reviews", classes="text-h1 text-center	")
    p1 = jp.QDiv(a=wp, text = "Graphs of the course")

    return wp

jp.justpy(app, port=8900)
