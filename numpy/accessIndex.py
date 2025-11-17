import numpy as np

array1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("1st row elements of array 1:", array1[0])
print("2nd row elements of array 1:", array1[1])
print("1st column elements of array 1:", array1[:, 0])
print("2nd column elements of array 1:", array1[:, 1])
print("1st to 4th column elements of array 1:", array1[:, 0:4])