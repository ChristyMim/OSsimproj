import numpy as np
from queue import *
from stack import *

array1 = np.random.randint(0, 100, 100)
array2 = np.random.randint(0, 100, 100)
array3 = np.random.randint(0, 100, 100)
array4 = np.random.randint(0, 100, 100)
array5 = np.random.randint(1, 4, 100)

# f = open("output.txt", "w")
#
# print(array1, file=f)
# print(file=f)
#
# print(array2, file=f)
# print(file=f)
#
# print(array3, file=f)
# print(file=f)
#
# print(array4, file=f)
# print(file=f)
#
# print(array5, file=f)
# f.close()

myQueue = My_Queue()
myStack = My_Stack()

if __name__ == '__main__':

    for data in array1:
        myQueue.enqueue(array1[data])

    myQueue.printqueue()
    print('\n')

    for data in array2:
        myStack.push(array2[data])

    myStack.printstack()
    print('\n')



