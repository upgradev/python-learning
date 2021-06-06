# there are a number of mathematical operations which could be performed with Numpy arrays
# trigonometric function
# logarithmic
# inverse
# exponential
# stattistical

import numpy as np

arr = np.array([1, 3, 5, 2, 6])

# cosine value of each element of the array
print(np.cos(arr))
print(np.log(arr))
print("mean: ", np.mean(arr))
print("median: ", np.median(arr))
print("std: ", np.std(arr))
print("exp: ", np.exp(arr))

arr1 = np.array([2, 4, 6, 8, 2])
arr2 = np.array([3, 6, 1, 5, 2])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
