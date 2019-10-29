import numpy as np
from queue import My_Queue

array1 = np.random.randint(0, 100, (10, 10))
array2 = np.random.randint(0, 100, (10, 10))
array3 = np.random.randint(0, 100, (10, 10))
array4 = np.random.randint(0, 100, (10, 10))
array5 = np.random.randint(1, 4, (10, 10))

f = open("output.txt", "w")
print(array1, file=f)
print(file=f)

print(array2, file=f)
print(file=f)

print(array3, file=f)
print(file=f)

print(array4, file=f)
print(file=f)

print(array5, file=f)
f.close()

if __name__ == '__main__':

    q = My_Queue()
    q.enqueue(array1)
    q.printqueue()

