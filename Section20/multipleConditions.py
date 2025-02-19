import pandas

data = pandas.read_csv("./Section20/data/reviews.csv")

result = data[(data["Rating"] > 4) & (data["Course Name"] == "The Complete Python Course: Build 10 Professional OOP Apps")]
print(result)
print("-----------------------------------------")
