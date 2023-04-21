import random
import time
import matplotlib.pyplot as plt

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    start_time = time.time()
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return time.time() - start_time
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return time.time() - start_time

def sequential_search(arr, x):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == x:
            return time.time() - start_time
    return time.time() - start_time

sizes = []
binary_times = []
sequential_times = []
for i in range(100):
    size = random.randint(1, 1000)
    arr = sorted([random.randint(0, 1000) for j in range(size)])
    x = random.randint(0, 1000)
    binary_time = binary_search(arr, x)
    binary_times.append(binary_time)
    sequential_time = sequential_search(arr, x)
    sequential_times.append(sequential_time)
    sizes.append(size)
    
plt.plot(sizes, binary_times, 'o', label='Binary Search')
plt.plot(sizes, sequential_times, 'o', label='Sequential Search')
plt.xlabel('Size of Input List')
plt.ylabel('Running Time (Seconds)')
plt.legend()
plt.show()

