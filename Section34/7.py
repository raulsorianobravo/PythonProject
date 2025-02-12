# Certain Passwords Only
# Loop over the items of the passwords list and in each iteration print out the item if the item contains the strings 'ba' or 'ab' inside.

# Just so that you know, such items are baaded, nbbaa, naadeba, naba, nabc, and nab.

passwords = ['ccavfb', 'baaded', 'bbaa', 'aaeed', 'vbb', 'aadeba', 'aba', 'dee', 'dade', 'abc', 'aae', 'dded', 'abb', 'aaf', 'ffaec']

x = [ i for i in passwords if str.__contains__(i,'ba')  or str.__contains__(i,'ab') ]
print(x)

for i in passwords:
    if str.__contains__(i,'ba')  or str.__contains__(i,'ab'):
        print(i)