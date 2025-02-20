import pandas
from datetime import datetime
from pytz import utc
data = pandas.read_csv("./Section20/data/reviews.csv", parse_dates=["Timestamp"])

import matplotlib.pyplot as plt

#day_avg = data.groupby(["Timestamp"])

data["Day"] = data["Timestamp"].dt.date
print(data)
print("-----------------------------------------")

#                                              Course Name                 Timestamp  Rating Comment         Day
# 0      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 06:25:52+00:00     4.0     NaN  2021-04-02
# 1      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:12:34+00:00     4.0     NaN  2021-04-02
# 2      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:11:03+00:00     4.0     NaN  2021-04-02
# 3      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:33:24+00:00     5.0     NaN  2021-04-02
# 4      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:31:49+00:00     4.5     NaN  2021-04-02
# ...                                                  ...                       ...     ...     ...         ...
# 44995                 Python for Beginners with Examples 2018-01-01 01:11:26+00:00     4.0     NaN  2018-01-01
# 44996  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:09:56+00:00     5.0     NaN  2018-01-01
# 44997  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:08:11+00:00     5.0     NaN  2018-01-01
# 44998                 Python for Beginners with Examples 2018-01-01 01:05:26+00:00     5.0     NaN  2018-01-01
# 44999  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:01:16+00:00     5.0     NaN  2018-01-01

# [45000 rows x 5 columns]


day_avg = data.iloc[:,2:].drop(columns=["Comment"])

print(day_avg)
print("-----------------------------------------")

#        Rating Comment         Day
# 0         4.0     NaN  2021-04-02
# 1         4.0     NaN  2021-04-02
# 2         4.0     NaN  2021-04-02
# 3         5.0     NaN  2021-04-02
# 4         4.5     NaN  2021-04-02
# ...       ...     ...         ...
# 44995     4.0     NaN  2018-01-01
# 44996     5.0     NaN  2018-01-01
# 44997     5.0     NaN  2018-01-01
# 44998     5.0     NaN  2018-01-01
# 44999     5.0     NaN  2018-01-01

# [45000 rows x 3 columns]
# -----------------------------------------

result = day_avg.groupby(["Day"])
print(result.first())
print("-----------------------------------------")


result = day_avg.groupby(["Day"]).mean()
print(result)
print("-----------------------------------------")

## Columns

print(result.columns)
print("-----------------------------------------")

# Index(['Rating'], dtype='object') 

print(result["Rating"])
print("-----------------------------------------")

print(result.index)
print("-----------------------------------------")

# -----------------------------------------
# Index([2018-01-01, 2018-01-02, 2018-01-03, 2018-01-04, 2018-01-05, 2018-01-06,
#        2018-01-07, 2018-01-08, 2018-01-09, 2018-01-10,
#        ...
#        2021-03-24, 2021-03-25, 2021-03-26, 2021-03-27, 2021-03-28, 2021-03-29,
#        2021-03-30, 2021-03-31, 2021-04-01, 2021-04-02],
#       dtype='object', name='Day', length=1188)
# -----------------------------------------


#print(list(result.index))

plt.plot(result.index, result["Rating"])
plt.show()
print("-----------------------------------------")

