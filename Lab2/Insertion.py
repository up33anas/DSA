import time
from funcs import RandomArray, InsertionSort, writeToCSV

arr = RandomArray(30000)
start = time.time()
InsertionSort(arr, 0, len(arr))
print("Time taken to run:", time.time() - start)
writeToCSV(arr, "SortedInsertionSort.csv")
