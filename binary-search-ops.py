import random
import matplotlib.pyplot as plt

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

sizes = []
ops = []
for i in range(100):
    size = random.randint(1, 1000)
    arr = sorted([random.randint(0, 1000) for j in range(size)])
    x = random.randint(0, 1000)
    idx = sequential_search(arr, x)
    sizes.append(size)
    ops.append(idx + 1 if idx != -1 else size)
    
plt.plot(sizes, ops, 'o')
plt.xlabel('Size of Input List')
plt.ylabel('Number of Operations')
plt.show()
