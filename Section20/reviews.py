import pandas

data = pandas.read_csv("./Section20/data/reviews.csv")

print(data)
print(data.head())
print(data.shape)
print(data.columns)
print(data.index)

# 0  The Python Mega Course: Build 10 Real World Ap...  2021-04-02 06:25:52+00:00     4.0     NaN
# 1  The Python Mega Course: Build 10 Real World Ap...  2021-04-02 05:12:34+00:00     4.0     NaN
# 2  The Python Mega Course: Build 10 Real World Ap...  2021-04-02 05:11:03+00:00     4.0     NaN
# 3  The Python Mega Course: Build 10 Real World Ap...  2021-04-02 03:33:24+00:00     5.0     NaN
# 4  The Python Mega Course: Build 10 Real World Ap...  2021-04-02 03:31:49+00:00     4.5     NaN

# (45000, 4)

# Index(['Course Name', 'Timestamp', 'Rating', 'Comment'], dtype='object')

# RangeIndex(start=0, stop=45000, step=1)

print(data.hist('Rating'))

##Select a column
rating_c = data["Rating"]
print(rating_c)

# 0        4.0
# 1        4.0
# 2        4.0
# 3        5.0
# 4        4.5
#         ...
# 44995    4.0
# 44996    5.0
# 44997    5.0
# 44998    5.0
# 44999    5.0
# Name: Rating, Length: 45000, dtype: float64


print(rating_c.mean())
# 4.442155555555556

#Select multiple columns

mult = data[["Course Name", "Rating"]]
print(mult)

#                                              Course Name  Rating
# 0      The Python Mega Course: Build 10 Real World Ap...     4.0
# 1      The Python Mega Course: Build 10 Real World Ap...     4.0
# 2      The Python Mega Course: Build 10 Real World Ap...     4.0
# 3      The Python Mega Course: Build 10 Real World Ap...     5.0
# 4      The Python Mega Course: Build 10 Real World Ap...     4.5
# ...                                                  ...     ...
# 44995                 Python for Beginners with Examples     4.0
# 44996  The Python Mega Course: Build 10 Real World Ap...     5.0
# 44997  The Python Mega Course: Build 10 Real World Ap...     5.0
# 44998                 Python for Beginners with Examples     5.0
# 44999  The Python Mega Course: Build 10 Real World Ap...     5.0

# [45000 rows x 2 columns]

# Select a Row

print(data.iloc[3])

# Course Name    The Python Mega Course: Build 10 Real World Ap...
# Timestamp                              2021-04-02 03:33:24+00:00
# Rating                                                       5.0
# Comment                                                      NaN
# Name: 3, dtype: object

# Select multiple rows

print(data.iloc[1:3])

#                                          Course Name                  Timestamp  Rating Comment
# 1  The Python Mega Course: Build 10 Real World Ap...  2021-04-02 05:12:34+00:00     4.0     NaN
# 2  The Python Mega Course: Build 10 Real World Ap...  2021-04-02 05:11:03+00:00     4.0     NaN

# Select a section

print(data[["Course Name", "Rating"]].iloc[1:3])

#                                          Course Name  Rating
# 1  The Python Mega Course: Build 10 Real World Ap...     4.0
# 2  The Python Mega Course: Build 10 Real World Ap...     4.0

# Select a cell

print(data["Timestamp"].iloc[2])

# 2021-04-02 05:11:03+00:00

print(data["Rating"].iloc[2])

# 4.0

print(data.at[2,"Rating"])

# 4.0
