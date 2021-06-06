import numpy as np

# ones function
arr = np.ones(2)
print("ones: ",arr)

print("ones: ",np.ones((2,2)))

# zeros 
print("zeros: ",np.zeros(2))

print("zeros: ",np.zeros((2,2)))

print("eye: ", np.eye(2,2))

# around 
arr = np.array([1.432,3.087,4.56])
print("around: ", np.around(arr))

print("around: ", np.around(arr, 2))

print("linspace: ", np.linspace(0,10,5))