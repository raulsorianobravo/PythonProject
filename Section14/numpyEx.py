#Numpy and OpenCV
import numpy as np

n = np.arange(27)
print(n , type(n))
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
#  24 25 26] <class 'numpy.ndarray'>

n3=n.reshape(3,9)
print(n3, type(n3))

# [[ 0  1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16 17]
#  [18 19 20 21 22 23 24 25 26]] <class 'numpy.ndarray'>

n3_3 = n.reshape(3,3,3)
print(n3_3, type(n3_3))

# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]

#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]

#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]] <class 'numpy.ndarray'>