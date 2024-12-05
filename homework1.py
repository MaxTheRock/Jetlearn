import numpy as np

# 1D Array
array_1d = np.array([1, 2, 3, 4, 5])
print(array_1d)

# 2D Array
array_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array_2d)

# 3D Array
array_3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
print(array_3d)

print(array_2d[0,1])
print(array_1d[2] + array_1d[3])
print(array_2d[0,0:3])
print(array_3d[0,1,0:2])
print()
print(array_2d[0:2,1:4])
print(array_1d.dtype)

array1 = np.array(["Apple","Banana","Grape"])
print(array1.dtype)
array2 = np.array(["String",123])
print(array2.dtype)
array3 = np.array([1.2, 1.2, 1.3, 1.4, 1.5])
print(array3.dtype)
new_array = array3.astype('b') # astype is a function that makes a copy of an array, and it's the best way to change the data type of existing array - you can type 'i' or int
print(new_array.dtype)
a1 = array3.copy()# Doesn't get affected and only shows the new array
a2 = array3.view()# Gets affected and shows original array
array3[0] = 4.5
print(a1)
print(a2)