import random, csv, time

def RandomArray(size):
    return [random.randint(0, 100000) for _ in range(size)]

def BubbleSort(array,start, end):
    n = end - start                # length of subarray
    for i in range(n - 1):
        swapped = False
        for j in range(start, start + n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array

def writeToCSV(arr, filename):
    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file)
        for item in arr:
            writer.writerow([item])

arr = RandomArray(30000)
start = time.time()
BubbleSort(arr, 0, len(arr))
print("Time taken to run:", time.time() - start)
writeToCSV(arr, "SortedBubbleSort.csv")
