#Install Panda
#pip install pandas

#install ipython
#pip install ipython

import pandas

df1 = pandas.DataFrame([[2,3,4],[43,5,22]])
print(df1)
#     0  1   2
# 0   2  3   4
# 1  43  5  22

df1 = pandas.DataFrame([[2,3,4],[43,5,22]], columns=["A","b","C"], index=["1","2"])
print(df1)
#     A  b   C
# 1   2  3   4
# 2  43  5  22

df2 = pandas.DataFrame([{"Name":"Raul"},{"Name":"Maria"},{"Name":"John"}])
print(df2)
#     Name
# 0   Raul
# 1  Maria
# 2   John

df3 = pandas.DataFrame([{"Name":"Raul","Age":44},{"Name":"Maria","Age":42},{"Name":"John","Age":22}])
print(df3)
#     Name  Age
# 0   Raul   44
# 1  Maria   42
# 2   John   22

print(type(df1))
#<class 'pandas.core.frame.DataFrame'>

print(df1.mean())
#the mean of every column
# A    22.5
# b     4.0
# C    13.0
#dtype: float64

print(df1.mean().mean())
#13.166666666666666

print(df1.A)
# 1     2
# 2    43
# Name: A, dtype: int64

print(df1.A.mean())
#22.5

print(df1.A.max())
#43