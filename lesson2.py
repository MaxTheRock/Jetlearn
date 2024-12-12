import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8])

array2 = array1[1:8:2]
print(array2)

array3 = array1[::-1]
print(array3)

array4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array4[0:1,0:1])

print(array4[0:1,2:3])
print(array4[1:2,0:3])

array5 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(array5[0:1,1:2,0:1])

even_array = array1[array1%2 == 0]
print(even_array)

bool_array = array1[array1 == 5]
print(bool_array)

print(array1[[2,4,6]])

array10 = np.array([1,2,3,4,5,6,7,8,9,10])
print()

print(array10[array10<5])

array1 = np.array([1,2,3,4,5,6,7,8])

array1 += 2
print(array1)
print()
array2 = np.array([1,2,3,4,5,6,7,8])
print(array1+array2)
