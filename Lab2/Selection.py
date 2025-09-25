import time
from funcs import RandomArray, SelectionSort, writeToCSV

arr = RandomArray(30000)

start = time.time()
SelectionSort(arr, 0, len(arr))
print("Time taken to run:", time.time() - start, "seconds")

writeToCSV(arr, "SortedSelectionSort.csv")