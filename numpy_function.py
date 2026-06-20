import numpy as np

"""a = np.array([
    [1,2,4],
             [3, 5,8]
            ] )

total = np.amin(a)
# amin for min value 
print(total)"""

"""python_list = [3,7,5,4,2,1]
numpy_arrary = np.array(python_list)
print(numpy_arrary)"""

'''x_list = list(range(10000))
y_list = list(range(10000))
x = np.array(x_list)
y = np.array(y_list)

n = np.array([2,4,6,8,10])

def add():
    z = []
    for i in range(len(x)):
        z.append(x[i]+y[i])'''

arr = np.array([3,8,7,3,5])
print(arr)
add = np.append(arr, 30)
print(add)
remove = np.delete(arr, 3)
print(remove)


