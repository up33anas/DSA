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

def writeToCSV(arr, filename):
    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file)
        for item in arr:
            writer.writerow([item])

arr = RandomArray(30000)
start = time.time()
InsertionSort(arr, 0, len(arr))
print("Time taken to run:", time.time() - start)
writeToCSV(arr, "SortedInsertionSort.csv")
