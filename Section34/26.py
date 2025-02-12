
# Decimal Universe
# Print out all numbers from 0 to 10 with an increment of 0.1.

# Expected output:

# 0
# 0.1
# 0.2
# ...
# 9.8
# 9.9
# 10.0

x=0.0
while x < 10.0:
    x = x + 0.1
    print(float(x))

for i in (x / 10 for x in range(0, 101)):
    print(i)