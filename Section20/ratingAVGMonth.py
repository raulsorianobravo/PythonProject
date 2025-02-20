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

data["Month"] = data["Timestamp"].dt.month
print(data)
print("-----------------------------------------")

#                                              Course Name                 Timestamp  Rating Comment         Day  Week
# 0      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 06:25:52+00:00     4.0     NaN  2021-04-02    13
# 1      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:12:34+00:00     4.0     NaN  2021-04-02    13
# 2      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:11:03+00:00     4.0     NaN  2021-04-02    13
# 3      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:33:24+00:00     5.0     NaN  2021-04-02    13
# 4      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:31:49+00:00     4.5     NaN  2021-04-02    13
# ...                                                  ...                       ...     ...     ...         ...   ...
# 44995                 Python for Beginners with Examples 2018-01-01 01:11:26+00:00     4.0     NaN  2018-01-01     1
# 44996  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:09:56+00:00     5.0     NaN  2018-01-01     1
# 44997  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:08:11+00:00     5.0     NaN  2018-01-01     1
# 44998                 Python for Beginners with Examples 2018-01-01 01:05:26+00:00     5.0     NaN  2018-01-01     1
# 44999  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:01:16+00:00     5.0     NaN  2018-01-01     1

# [45000 rows x 6 columns]
# -----------------------------------------

print(data["Month"].max())

#53  --> group the week 1 of each year instead 1 week every year

data["Month"] = data["Timestamp"].dt.strftime('%Y-%m')
print(data)
print("-----------------------------------------")

#                                              Course Name                 Timestamp  Rating Comment         Day     Week
# 0      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 06:25:52+00:00     4.0     NaN  2021-04-02  2021-13
# 1      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:12:34+00:00     4.0     NaN  2021-04-02  2021-13
# 2      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:11:03+00:00     4.0     NaN  2021-04-02  2021-13
# 3      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:33:24+00:00     5.0     NaN  2021-04-02  2021-13
# 4      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:31:49+00:00     4.5     NaN  2021-04-02  2021-13
# ...                                                  ...                       ...     ...     ...         ...      ...
# 44995                 Python for Beginners with Examples 2018-01-01 01:11:26+00:00     4.0     NaN  2018-01-01  2018-00
# 44996  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:09:56+00:00     5.0     NaN  2018-01-01  2018-00
# 44997  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:08:11+00:00     5.0     NaN  2018-01-01  2018-00
# 44998                 Python for Beginners with Examples 2018-01-01 01:05:26+00:00     5.0     NaN  2018-01-01  2018-00
# 44999  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:01:16+00:00     5.0     NaN  2018-01-01  2018-00

# [45000 rows x 6 columns]
# -----------------------------------------

month_average = data.groupby(["Month"]).mean(numeric_only=True)

print(month_average)
print("-----------------------------------------")

#            Rating
# Week
# 2018-00  4.434564
# 2018-01  4.424933
# 2018-02  4.417702
# 2018-03  4.401024
# 2018-04  4.468085
# ...           ...
# 2021-09  4.560096
# 2021-10  4.627315
# 2021-11  4.629121
# 2021-12  4.607843
# 2021-13  4.429032

# [173 rows x 1 columns]
# -----------------------------------------

plt.figure(figsize=(25,3))
plt.plot(month_average.index, month_average["Rating"]) 
plt.show()
print("-----------------------------------------")