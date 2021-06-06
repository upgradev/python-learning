# numpy arrays 
# numpy aims to provide an array object tat is up to 50 times faster than traditional python list

import numpy as np

# creating 1-d array
ar = np.array([1,4,6,3,7])
print(ar)

ar2 = np.array([2,3,4,5])
print(ar2)

arr = np.array([[1,2,4], [5,6,8]])
print(arr)

arr = np.array([[1,2,4], [5,6,8], [1,2,4], [5,6,7]])
print(arr)

ar = np.array([1,4,6,3,7])
print(ar[2])

arr = np.array([[1,2,4], [5,6,8]])
print(arr[0,1])