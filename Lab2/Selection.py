import random, csv, time

def RandomArray(size):
    return [random.randint(0, 100000) for _ in range(size)]

def SelectionSort(array, start, end):
    for i in range(start, end - 1):
        minIndex = i 
        for j in range(i + 1, end):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array

def writeToCSV(arr, filename):
    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file)
        for item in arr:
            writer.writerow([item])

arr = RandomArray(30000)
start = time.time()
SelectionSort(arr, 0, len(arr))
print("Time taken to run:", time.time() - start)
writeToCSV(arr, "SortedSelectionSort.csv")
