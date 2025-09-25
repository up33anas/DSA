import time
from funcs import RandomArray, BubbleSort, writeToCSV

arr = RandomArray(30000)

start = time.time()
BubbleSort(arr, 0, len(arr))
print("Time taken to run:", time.time() - start, "seconds")

writeToCSV(arr, "SortedBubbleSort.csv")
