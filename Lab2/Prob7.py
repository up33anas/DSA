import time, csv
from funcs import RandomArray, InsertionSort, MergeSort, HybridMergeSort, SelectionSort, BubbleSort

# Read all n values
with open("Nvalues.txt") as file:
    n_values = [int(line.strip()) for line in file if line.strip()]

allRunTimes = []

for n in n_values:
    base = RandomArray(n)
    runTimes = [n]

    # Insertion Sort
    arr = base.copy()
    start = time.perf_counter()
    InsertionSort(arr, 0, len(arr) - 1)
    runTimes.append(round(time.perf_counter() - start, 6))

    # Merge Sort
    arr = base.copy()
    start = time.perf_counter()
    MergeSort(arr, 0, len(arr) - 1)
    runTimes.append(round(time.perf_counter() - start, 6))

    # Hybrid Merge Sort
    arr = base.copy()
    start = time.perf_counter()
    HybridMergeSort(arr, 0, len(arr) - 1, 32)
    runTimes.append(round(time.perf_counter() - start, 6))

    # Selection Sort
    arr = base.copy()
    start = time.perf_counter()
    SelectionSort(arr, 0, len(arr) - 1)
    runTimes.append(round(time.perf_counter() - start, 6))

    # Bubble Sort
    arr = base.copy()
    start = time.perf_counter()
    BubbleSort(arr, 0, len(arr) - 1)
    runTimes.append(round(time.perf_counter() - start, 6))

    print(f"Done for n={n}: {runTimes[1:]}")
    allRunTimes.append(runTimes)

headers = [
    "Value of n",
    "Insertion Sort (seconds)",
    "Merge Sort (seconds)",
    "Hybrid Merge Sort (seconds)",
    "Selection Sort (seconds)",
    "Bubble Sort (seconds)"
]

with open("RunTime.csv", "w", newline="", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerow(headers)
      writer.writerows(allRunTimes)
