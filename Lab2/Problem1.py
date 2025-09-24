import random, csv, time

def RandomArray(size):
    return [random.randint(0, 100000) for _ in range(size)]

def writeToCSV(arr, filename):
    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file)
        for item in arr: 
            writer.writerow([item])

start = time.time()
r = RandomArray(100)
print("To run", time.time() - start)
writeToCSV(r, "one.csv")
