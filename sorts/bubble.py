import random

arr = [random.randint(-100, 100) for _ in range(10)]
print(arr)

for i in range(len(arr) - 1):
    for  j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)