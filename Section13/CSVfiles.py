import os
import pandas

os.listdir()

df1 = pandas.read_csv("./Section13/files/supermarkets/supermarkets.csv")
print(df1)

#    ID          Address           City             State Country         Name  Employees
# 0   1     3666 21st St  San Francisco          CA 94114     USA      Madeira          8
# 1   2   735 Dolores St  San Francisco          CA 94119     USA  Bready Shop         15
# 2   3      332 Hill St  San Francisco  California 94114     USA  Super River         25
# 3   4     3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop         10
# 4   5  1056 Sanchez St  San Francisco        California     USA      Sanchez         12
# 5   6  551 Alvarado St  San Francisco          CA 94114     USA   Richvalley         20

df2 = pandas.read_json("./Section13/files/supermarkets/supermarkets.json")
print(df2)

#    ID          Address           City             State Country         Name  Employees
# 0   1     3666 21st St  San Francisco          CA 94114     USA      Madeira          8
# 1   2   735 Dolores St  San Francisco          CA 94119     USA  Bready Shop         15
# 2   3      332 Hill St  San Francisco  California 94114     USA  Super River         25
# 3   4     3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop         10
# 4   5  1056 Sanchez St  San Francisco        California     USA      Sanchez         12
# 5   6  551 Alvarado St  San Francisco          CA 94114     USA   Richvalley         20

df3= pandas.read_excel("./Section13/files/supermarkets/supermarkets.xlsx", sheet_name=0)
print(df3)

#    ID          Address           City             State Country Supermarket Name  Number of Employees
# 0   1     3666 21st St  San Francisco          CA 94114     USA          Madeira                    8
# 1   2   735 Dolores St  San Francisco          CA 94119     USA      Bready Shop                   15
# 2   3      332 Hill St  San Francisco  California 94114     USA      Super River                   25
# 3   4     3995 23rd St  San Francisco          CA 94114     USA       Ben's Shop                   10
# 4   5  1056 Sanchez St  San Francisco        California     USA          Sanchez                   12
# 5   6  551 Alvarado St  San Francisco          CA 94114     USA       Richvalley                   20

df4=pandas.read_csv("./Section13/files/supermarkets/supermarkets-commas.txt")
print(df4)

#    ID          Address           City             State Country         Name  Employees
# 0   1     3666 21st St  San Francisco          CA 94114     USA      Madeira          8
# 1   2   735 Dolores St  San Francisco          CA 94119     USA  Bready Shop         15
# 2   3      332 Hill St  San Francisco  California 94114     USA  Super River         25
# 3   4     3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop         10
# 4   5  1056 Sanchez St  San Francisco        California     USA      Sanchez         12
# 5   6  551 Alvarado St  San Francisco          CA 94114     USA   Richvalley         20

#With separators
df5=pandas.read_csv("./Section13/files/supermarkets/supermarkets-semi-colons.txt", sep=";")
print(df5)

#    ID          Address           City             State Country          Name  Employees
# 0   1     3666 21st St  San Francisco          CA 94114     USA       Madeira          8
# 1   2   735 Dolores St  San Francisco          CA 94119     USA   Bready Shop         15
# 2   3      332 Hill St  San Francisco  California 94114     USA   Super River         25
# 3   4     3995 23rd St  San Francisco          CA 94114     USA    Ben's Shop         10
# 4   5  1056 Sanchez St  San Francisco        California     USA       Sanchez         12
# 5   6  551 Alvarado St  San Francisco          CA 94114     USA    Richvalley         20

#Without Headers
df8=pandas.read_csv("./Section13/files/supermarkets/supermarkets.csv", header=None)
print("df8\n", df8)

#      0                1              2                 3        4            5          6
# 0  ID          Address           City             State  Country         Name  Employees
# 1   1     3666 21st St  San Francisco          CA 94114      USA      Madeira          8
# 2   2   735 Dolores St  San Francisco          CA 94119      USA  Bready Shop         15
# 3   3      332 Hill St  San Francisco  California 94114      USA  Super River         25
# 4   4     3995 23rd St  San Francisco          CA 94114      USA   Ben's Shop         10
# 5   5  1056 Sanchez St  San Francisco        California      USA      Sanchez         12
# 6   6  551 Alvarado St  San Francisco          CA 94114      USA   Richvalley         20

#Assign Columns names
df8.columns = ["ID", "Address", "City", "zip", "Country", "Name", "Employess"]
print("df8\n", df8)

# df8
#     ID          Address           City               zip  Country         Name  Employess
# 0  ID          Address           City             State  Country         Name  Employees
# 1   1     3666 21st St  San Francisco          CA 94114      USA      Madeira          8
# 2   2   735 Dolores St  San Francisco          CA 94119      USA  Bready Shop         15
# 3   3      332 Hill St  San Francisco  California 94114      USA  Super River         25
# 4   4     3995 23rd St  San Francisco          CA 94114      USA   Ben's Shop         10
# 5   5  1056 Sanchez St  San Francisco        California      USA      Sanchez         12
# 6   6  551 Alvarado St  San Francisco          CA 94114      USA   Richvalley         20


#SET Index. Show since the coulumn selected
df9=pandas.read_csv("./Section13/files/supermarkets/supermarkets.csv")
df9_= df9.set_index("ID")
print("df9_\n", df9_ ,"\ndf9\n", df9)

# df9_
#              Address           City             State Country         Name  Employees
# ID
# 1      3666 21st St  San Francisco          CA 94114     USA      Madeira          8
# 2    735 Dolores St  San Francisco          CA 94119     USA  Bready Shop         15
# 3       332 Hill St  San Francisco  California 94114     USA  Super River         25
# 4      3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop         10
# 5   1056 Sanchez St  San Francisco        California     USA      Sanchez         12
# 6   551 Alvarado St  San Francisco          CA 94114     USA   Richvalley         20
# df9
#     ID          Address           City             State Country         Name  Employees
# 0   1     3666 21st St  San Francisco          CA 94114     USA      Madeira          8
# 1   2   735 Dolores St  San Francisco          CA 94119     USA  Bready Shop         15
# 2   3      332 Hill St  San Francisco  California 94114     USA  Super River         25
# 3   4     3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop         10
# 4   5  1056 Sanchez St  San Francisco        California     USA      Sanchez         12
# 5   6  551 Alvarado St  San Francisco          CA 94114     USA   Richvalley         20

# overwrite the index 
df10=pandas.read_csv("./Section13/files/supermarkets/supermarkets.csv")
df10.set_index("ID", inplace=True)
print("df10\n", df10)

# df10
#              Address           City             State Country         Name  Employees
# ID
# 1      3666 21st St  San Francisco          CA 94114     USA      Madeira          8
# 2    735 Dolores St  San Francisco          CA 94119     USA  Bready Shop         15
# 3       332 Hill St  San Francisco  California 94114     USA  Super River         25
# 4      3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop         10
# 5   1056 Sanchez St  San Francisco        California     USA      Sanchez         12
# 6   551 Alvarado St  San Francisco          CA 94114     USA   Richvalley         20

# Delete the index column an set Address. Lost the columns Address as values

df11=pandas.read_csv("./Section13/files/supermarkets/supermarkets.csv")
df11.set_index("Address", inplace=True)
print("df11\n", df11)

# df11
#                   ID           City             State Country         Name  Employees
# Address
# 3666 21st St      1  San Francisco          CA 94114     USA      Madeira          8
# 735 Dolores St    2  San Francisco          CA 94119     USA  Bready Shop         15
# 332 Hill St       3  San Francisco  California 94114     USA  Super River         25
# 3995 23rd St      4  San Francisco          CA 94114     USA   Ben's Shop         10
# 1056 Sanchez St   5  San Francisco        California     USA      Sanchez         12
# 551 Alvarado St   6  San Francisco          CA 94114     USA   Richvalley         20

# Keep columns
df11=pandas.read_csv("./Section13/files/supermarkets/supermarkets.csv")
df11.set_index("Employees", inplace=True, drop=False)
print("df11\n", df11)

# df11
#             ID          Address           City             State Country         Name  Employees
# Employees
# 8           1     3666 21st St  San Francisco          CA 94114     USA      Madeira          8
# 15          2   735 Dolores St  San Francisco          CA 94119     USA  Bready Shop         15
# 25          3      332 Hill St  San Francisco  California 94114     USA  Super River         25
# 10          4     3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop         10
# 12          5  1056 Sanchez St  San Francisco        California     USA      Sanchez         12
# 20          6  551 Alvarado St  San Francisco          CA 94114     USA   Richvalley         20

