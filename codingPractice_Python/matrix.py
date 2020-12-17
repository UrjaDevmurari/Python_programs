# sum of all elements of matrix
import numpy as np

m1 = [[1, 2],
      [3, 4],
      [8, 4]]
total = 0
for i in m1:
    for j in i:
        total = total + j
print(total)
print("Sum of all column elements is: {}".format(np.sum(m1, axis=0)))
print("Sum of all row elements is: {}".format(np.sum(m1, axis=1)))
print("Sum of all row elements and preserving the dimensions: \n{}".format(np.sum(m1, axis=1, keepdims=True)))
