import numpy as np

my_list = [1, 2, 3]
type(my_list)
print(list)

myarray = np.array(my_list)
print(myarray)
type(myarray)

# print(np.arange(begin,end,step))
print(np.arange(0, 10, 2))

# array of zeros
# print(np.zeros(shape=(row,column)))
# float numbers
print(np.zeros(shape=(5, 5)))

# array of ones
print(np.ones(shape=(2, 4)))

np.random.seed(101)
arr = np.random.randint(0,100,10)
print(arr)

arr2 = np.random.randint(0,100, 10)
print(arr2)

# find max and min of array and index
print(arr.max())
print(arr.argmax())
print(arr.min())
print(arr.argmin())