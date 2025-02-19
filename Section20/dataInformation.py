import pandas
from datetime import datetime
from pytz import utc
data = pandas.read_csv("./Section20/data/reviews.csv", parse_dates=["Timestamp"])

# Average rating

result = data["Rating"].mean()

print(result)
print("-----------------------------------------")

# 4.442155555555556
# -----------------------------------------

# Average rating for a particular course

result = data[data["Course Name"]=="The Python Mega Course: Build 10 Real World Applications"]["Rating"].mean()

print(result)
print("-----------------------------------------")

# 4.477270180942244
# -----------------------------------------

# Average rating for a particular period

result = data[(data["Timestamp"] >= datetime(2020,1,1, tzinfo=utc)) & (data["Timestamp"] <= datetime(2021,12,31, tzinfo=utc))]["Rating"].mean()

print(result)
print("-----------------------------------------")

# 4.490726587180271
# -----------------------------------------

# Average rating for a particular period and a course

result = data[(data["Timestamp"] >= datetime(2020,1,1, tzinfo=utc)) & (data["Timestamp"] <= datetime(2021,12,31, tzinfo=utc)) & (data["Course Name"]=="The Python Mega Course: Build 10 Real World Applications") ]["Rating"].mean()

print(result)
print("-----------------------------------------")

# 4.516905615292712
# -----------------------------------------

# Average of uncommented  and commented ratings

result = data[data["Comment"].isnull()]["Rating"].mean()
result2 = data[data["Comment"].notnull()]["Rating"].mean()

print(result, result2)
print("-----------------------------------------")

# 4.433679746603492 4.489777908515959
# -----------------------------------------

# Number of uncommented and commented ratings

result = data[data["Comment"].isnull()]["Rating"].count()
result2 = data[data["Comment"].notnull()]["Rating"].count()

print(result, result2)
print("-----------------------------------------")

# 38201 6799
# -----------------------------------------

# Number of comments containing a certain world
result = data[data["Comment"].str.contains("accent", na = False)]["Rating"].count()

print(result)
print("-----------------------------------------")

# 77
# -----------------------------------------

# Average of commented ratings with "accent" in comment

result = data[data["Comment"].str.contains("accent", na = False)]["Rating"].mean()

print(result)
print("-----------------------------------------")

# 3.8636363636363638
# -----------------------------------------