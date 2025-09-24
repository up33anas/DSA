import sys
import random, csv, time
sys.setrecursionlimit(50000)

def RandomArray(size):
    return [random.randint(0, 100000) for _ in range(size)]

def Merge(array, p, q, r):
    mergedArray = [] # empty temp array

    # p = start, q = mid, r = end
    i, j = p, q + 1 

    # merge the array
    while i <= q and j <= r:
        if array[i] <= array[j]:
            mergedArray.append(array[i])
            i += 1
        else: 
            mergedArray.append(array[j])
            j += 1
    
    # append the remaining elements of any array
    while i <= q:
        mergedArray.append(array[i])
        i += 1
    while j <= r:
        mergedArray.append(array[j])
        j += 1

    # copy temp array to the original one
    for i in range(len(mergedArray)):
        array[i + p] = mergedArray[i]
        
def MergeSort(array, start, end):
    if start < end: 
        mid = start + (end - start) // 2

        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)

        # merge two sorted parts
        Merge(array, start, mid, end)

def writeToCSV(arr, filename):
    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file)
        for item in arr:
            writer.writerow([item])

arr = RandomArray(30000)
start = time.time()
MergeSort(arr, 0, len(arr) - 1)
print("Time taken to run:", time.time() - start)
writeToCSV(arr, "SortedMergeSort.csv")