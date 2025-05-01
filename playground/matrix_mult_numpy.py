import numpy as np

# helper function to check matrix multiplication in numpy


a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([[2,0,0], [0,2,0], [0,0,2]])

# c = a @ b

# print(c)

x = np.array([
    [    0.0,    1.0,    2.0],
    [    3.0,    4.0,    5.0],
    [    6.0,    7.0,    8.0]
])
y = np.array([
[   -2.1,    5.3,    4.1],
[   11.6,   10.4,   17.8],
[   16.7,   24.1,   23.0]
])


z = x @ y 
print(z)


# C = A x B:
#    45.0   58.7   63.8
#   123.3  178.1  198.7
#   201.7  297.6  333.6
