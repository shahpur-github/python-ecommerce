import os
import numpy as np
import random
f = open('testcase1.txt', 'a')

f.write('this is the second line in the file \n ')
f.close()
f = open('testcase1.txt', 'r')
print(f.read())
f.close()
os.remove('testcase1.txt')
# 1D array
arr = np.array([1,2,3,4,5])

print(arr)
# 2D array
arr2d = np.array([[1,2,3,32,43],[4,5,6,43,21]])
print(arr2d.shape)

print(arr2d[1,-1])

# 3D array

arr3d = np.array([[[1,2,3,32,43],[4,5,6,43,21]],[[32,88,43,12,93],[43,32,12,12,54]]])

print(arr3d[0,1,3])

print(arr3d[1,1,1])
print(arr3d[:,1,:])
# all zeros and all ones array np.zeros((rows,colunms)) np.ones((rows,colunms))

arr0 =np.zeros((2,5,2))

print(arr0)

arrall1 =np.ones((2,5,3))

print(arrall1)

# np.full(rows,columns), data)
arrdata =np.full((3,5),21)
print(arrdata)


# random decimal numbers array

rannum = np.random.rand(5,4,2)

print('Randon numbers', rannum)

# random int numbers array

rannumin = np.random.randint(20, size=(4,3,3))

print('Randon int', rannumin)

arr5by5 = np.ones((6,5), type('int32'))

arr5by5[1:4,1:4] =2
arr5by5[2,2]=9
arr5by5[2:4,0:2]=5
arr5by5[[0,0,4,4,5,5],[3,4,3,4,3,4]]=7

#arr5by5[[0,4,5],[3:]]=7
print(arr5by5)
print('sorted \n', np.sort(arr5by5))

