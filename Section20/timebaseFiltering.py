# import pandas
# from datetime import datetime

# data = pandas.read_csv("./Section20/data/reviews.csv")

# # result = data[(data["Timestamp"] >= datetime(2020,7,1)) & (data["Timestamp"] <= datetime(2021,12,1))]
# #   File "ops.pyx", line 107, in pandas._libs.ops.scalar_compare
# # TypeError: '>' not supported between instances of 'str' and 'datetime.datetime'

# print(result)
# print("-----------------------------------------")


import pandas
from datetime import datetime
from pytz import utc
data = pandas.read_csv("./Section20/data/reviews.csv", parse_dates=["Timestamp"])



result = data[(data["Timestamp"] >= datetime(2020,7,1, tzinfo=utc)) & (data["Timestamp"] <= datetime(2021,12,7, tzinfo=utc))]

print(result)
print("-----------------------------------------")


#                                             Course Name                 Timestamp  Rating                                            Comment
# 0     The Python Mega Course: Build 10 Real World Ap... 2021-04-02 06:25:52+00:00     4.0                                                NaN
# 1     The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:12:34+00:00     4.0                                                NaN
# 2     The Python Mega Course: Build 10 Real World Ap... 2021-04-02 05:11:03+00:00     4.0                                                NaN
# 3     The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:33:24+00:00     5.0                                                NaN
# 4     The Python Mega Course: Build 10 Real World Ap... 2021-04-02 03:31:49+00:00     4.5                                                NaN
# ...                                                 ...                       ...     ...                                                ...
# 9729  The Python Mega Course: Build 10 Real World Ap... 2020-07-01 03:09:44+00:00     3.5                                                NaN
# 9730  The Python Mega Course: Build 10 Real World Ap... 2020-07-01 03:09:12+00:00     5.0                                                NaN
# 9731  The Python Mega Course: Build 10 Real World Ap... 2020-07-01 02:40:58+00:00     4.0                                                NaN
# 9732  The Python Mega Course: Build 10 Real World Ap... 2020-07-01 02:04:02+00:00     5.0                                               nice
# 9733  The Python Mega Course: Build 10 Real World Ap... 2020-07-01 00:01:34+00:00     2.0  Hard to follow if u have no experience program...

# [9734 rows x 4 columns]
# -----------------------------------------