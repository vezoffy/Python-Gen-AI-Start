import sys
import timeit
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sys.getsizeof(l), "bytes")
print(sys.getsizeof(t), "bytes")
y = timeit.timeit(stmt='[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', number=1000000)
print(y, "seconds")
x = timeit.timeit(stmt='(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)', number=1000000)  
print(x, "seconds")