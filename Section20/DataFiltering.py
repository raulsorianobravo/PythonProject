import pandas

data = pandas.read_csv("./Section20/data/reviews.csv")

result = data[data["Rating"] > 4]
print(result)
print(len(result))
print("-----------------------------------------")

#                                              Course Name                  Timestamp  Rating Comment
# 3      The Python Mega Course: Build 10 Real World Ap...  2021-04-02 03:33:24+00:00     5.0     NaN
# 4      The Python Mega Course: Build 10 Real World Ap...  2021-04-02 03:31:49+00:00     4.5     NaN
# 5      The Python Mega Course: Build 10 Real World Ap...  2021-04-02 01:10:06+00:00     4.5     NaN
# 6      The Python Mega Course: Build 10 Real World Ap...  2021-04-02 00:44:54+00:00     4.5     NaN
# 7      The Python Mega Course: Build 10 Real World Ap...  2021-04-01 23:42:02+00:00     5.0     NaN
# ...                                                  ...                        ...     ...     ...
# 44994  The Python Mega Course: Build 10 Real World Ap...  2018-01-01 01:19:24+00:00     5.0     NaN
# 44996  The Python Mega Course: Build 10 Real World Ap...  2018-01-01 01:09:56+00:00     5.0     NaN
# 44997  The Python Mega Course: Build 10 Real World Ap...  2018-01-01 01:08:11+00:00     5.0     NaN
# 44998                 Python for Beginners with Examples  2018-01-01 01:05:26+00:00     5.0     NaN
# 44999  The Python Mega Course: Build 10 Real World Ap...  2018-01-01 01:01:16+00:00     5.0     NaN

# [29758 rows x 4 columns]
#29758
# -----------------------------------------

result = data[data["Rating"] > 4].count()
print(result)
print(len(result))
print("-----------------------------------------")

# Course Name    29758
# Timestamp      29758
# Rating         29758
# Comment         4927
# dtype: int64
# 4
# -----------------------------------------

result = data[data["Rating"] > 4]["Rating"]
print(result)
print(len(result))
print("-----------------------------------------")

# 3        5.0
# 4        4.5
# 5        4.5
# 6        4.5
# 7        5.0
#         ...
# 44994    5.0
# 44996    5.0
# 44997    5.0
# 44998    5.0
# 44999    5.0
# Name: Rating, Length: 29758, dtype: float64
# 29758
# -----------------------------------------

result = data[data["Rating"] > 4]["Rating"].mean()
print(result)
print("-----------------------------------------")

# 4.87316015861281
# -----------------------------------------