import math

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def BucketSort(A: list):
    n = len(A)
    B = [[] for _ in  range(n)]

    for i in range(n):
        B[math.floor(n * A[i])].append(A[i])

    for i in range(n):
        B[i] = InsertionSort(B[i])

    A.clear()
    for i in range(n):
        A.extend(B[i])
        
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434] 

BucketSort(arr)
print(arr)