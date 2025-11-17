#Creatin n-D arrays
import numpy as np

list2 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
         [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]
array2 = np.array(list2)
print(array2)
print(array2.ndim)
print(array2.shape)
