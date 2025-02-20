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

#                                              Course Name                 Timestamp  Rating Comment         Day  Month
# 0      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 06:25:52+00:00     4.0     NaN  2021-04-02      4
# 1      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:12:34+00:00     4.0     NaN  2021-04-02      4
# 2      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:11:03+00:00     4.0     NaN  2021-04-02      4
# 3      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:33:24+00:00     5.0     NaN  2021-04-02      4
# 4      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:31:49+00:00     4.5     NaN  2021-04-02      4
# ...                                                  ...                       ...     ...     ...         ...    ...
# 44995                 Python for Beginners with Examples 2018-01-01 01:11:26+00:00     4.0     NaN  2018-01-01      1
# 44996  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:09:56+00:00     5.0     NaN  2018-01-01      1
# 44997  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:08:11+00:00     5.0     NaN  2018-01-01      1
# 44998                 Python for Beginners with Examples 2018-01-01 01:05:26+00:00     5.0     NaN  2018-01-01      1
# 44999  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:01:16+00:00     5.0     NaN  2018-01-01      1

# [45000 rows x 6 columns]
# -----------------------------------------

print(data["Month"].max())

#53  --> group the week 1 of each year instead 1 week every year

data["Month"] = data["Timestamp"].dt.strftime('%Y-%m')
print(data)
print("-----------------------------------------")

#                                              Course Name                 Timestamp  Rating Comment         Day    Month
# 0      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 06:25:52+00:00     4.0     NaN  2021-04-02  2021-04
# 1      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:12:34+00:00     4.0     NaN  2021-04-02  2021-04
# 2      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:11:03+00:00     4.0     NaN  2021-04-02  2021-04
# 3      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:33:24+00:00     5.0     NaN  2021-04-02  2021-04
# 4      The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:31:49+00:00     4.5     NaN  2021-04-02  2021-04
# ...                                                  ...                       ...     ...     ...         ...      ...
# 44995                 Python for Beginners with Examples 2018-01-01 01:11:26+00:00     4.0     NaN  2018-01-01  2018-01
# 44996  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:09:56+00:00     5.0     NaN  2018-01-01  2018-01
# 44997  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:08:11+00:00     5.0     NaN  2018-01-01  2018-01
# 44998                 Python for Beginners with Examples 2018-01-01 01:05:26+00:00     5.0     NaN  2018-01-01  2018-01
# 44999  The Python Mega Course: Build 10 Real World Ap... 2018-01-01 01:01:16+00:00     5.0     NaN  2018-01-01  2018-01

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

month_average_crs = data.groupby(["Month","Course Name"]).mean(numeric_only=True)
print(month_average_crs)
print("-----------------------------------------")

#                                                               Rating
# Month   Course Name
# 2018-01 100 Python Exercises I: Evaluate and Improve Yo...  4.353448
#         Data Processing with Python                         4.500000
#         Interactive Data Visualization with Python and ...  4.285714
#         Learn GIS in One Hour                               4.236842
#         Python for Beginners with Examples                  4.355422
# ...                                                              ...
# 2021-03 The Python Mega Course: Build 10 Real World App...  4.632018
# 2021-04 100 Python Exercises I: Evaluate and Improve Yo...  4.500000
#         Interactive Data Visualization with Python and ...  5.000000
#         The Complete Python Course: Build 10 Profession...  4.250000
#         The Python Mega Course: Build 10 Real World App...  4.576923

# [262 rows x 1 columns]
# -----------------------------------------

month_average_crs = data.groupby(["Month","Course Name"]).mean(numeric_only=True).unstack()
print(month_average_crs)
print("-----------------------------------------")

#                                                               Rating  ...
# Course Name 100 Python Exercises I: Evaluate and Improve Your Skills  ... The Python Mega Course: Build 10 Real World Applications
# Month                                                                 ...
# 2018-01                                               4.353448        ...                                           4.457368
# 2018-02                                               4.250000        ...                                           4.481070
# 2018-03                                               4.500000        ...                                           4.447037
# 2018-04                                               4.431034        ...                                           4.507412
# 2018-05                                               4.358696        ...                                           4.422085
# 2018-06                                               4.268293        ...                                           4.421264
# 2018-07                                               4.589286        ...                                           4.436156
# 2018-08                                               4.353659        ...                                           4.376494
# 2018-09                                               4.238636        ...                                           4.416413
# 2018-10                                               4.106061        ...                                           4.415292
# 2018-11                                               4.212766        ...                                           4.417481
# 2018-12                                               4.405172        ...                                           4.364149
# 2019-01                                               4.048780        ...                                           4.443763
# 2019-02                                               4.333333        ...                                           4.378671
# 2019-03                                               4.269231        ...                                           4.370213
# 2019-04                                               4.365854        ...                                           4.474803
# 2019-05                                               4.486111        ...                                           4.420777
# 2019-06                                               4.442308        ...                                           4.439291
# 2019-07                                               4.414634        ...                                           4.412245
# 2019-08                                               4.222222        ...                                           4.465208
# 2019-09                                               4.531250        ...                                           4.473086
# 2019-10                                               4.287500        ...                                           4.547354
# 2019-11                                               4.512195        ...                                           4.521374
# 2019-12                                               4.152778        ...                                           4.497470
# 2020-01                                               4.277778        ...                                           4.475647
# 2020-02                                               4.200000        ...                                           4.462660
# 2020-03                                               4.240000        ...                                           4.507212
# 2020-04                                               4.329268        ...                                           4.514571
# 2020-05                                               4.340909        ...                                           4.480292
# 2020-06                                               4.397059        ...                                           4.522647
# 2020-07                                               4.250000        ...                                           4.533848
# 2020-08                                               4.121622        ...                                           4.491681
# 2020-09                                               4.307692        ...                                           4.506821
# 2020-10                                               4.366667        ...                                           4.544296
# 2020-11                                               4.461538        ...                                           4.508387
# 2020-12                                               4.294118        ...                                           4.542740
# 2021-01                                               4.283333        ...                                           4.555494
# 2021-02                                               4.450000        ...                                           4.583846
# 2021-03                                               4.190476        ...                                           4.632018
# 2021-04                                               4.500000        ...                                           4.576923

# [40 rows x 8 columns]
# -----------------------------------------


plt.figure(figsize=(25,8))
plt.plot(month_average_crs.index, month_average_crs["Rating"]) 
plt.show()
print("-----------------------------------------")



month_average_crs = data.groupby(["Month","Course Name"])["Rating"].count().unstack()
print(month_average_crs)
print("-----------------------------------------")

plt.figure(figsize=(25,8))
plt.plot(month_average_crs.index, month_average_crs) 
plt.show()
print("-----------------------------------------")