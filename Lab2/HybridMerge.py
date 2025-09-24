import random, csv, time

def RandomArray(size):
    return [random.randint(0, 100000) for _ in range(size)]

def InsertionSort(array, start, end):
    for i in range(start + 1, end):
        key = array[i]
        j = i - 1
        # use array instead of arr, and respect start index
        while j >= start and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

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
        
def HybridMergeSort(array, start, end, k):
    if end - start + 1 <= k:       # size of this slice <= k
        InsertionSort(array, start, end + 1)  # end is exclusive in our InsertionSort
    return

    if start < end: 
        mid = start + (end - start) // 2

        HybridMergeSort(array, start, mid, k)
        HybridMergeSort(array, mid + 1, end, k)

        # merge two sorted parts
        Merge(array, start, mid, end)

def writeToCSV(arr, filename):
    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file)
        for item in arr:
            writer.writerow([item])

arr = RandomArray(30000)
start = time.time()
HybridMergeSort(arr, 0, len(arr) - 1, k=4000)
print("Time taken to run:", time.time() - start)
writeToCSV(arr, "SortedHybridSort.csv")