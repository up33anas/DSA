# Function
def SearchA(Arr, x):
    arr_of_indices = []
    for i in range(len(Arr)):
        if Arr[i] == x:
            arr_of_indices.append(i) 
        if Arr[i+1] > x: break
    return arr_of_indices

# Driver
X = [1,2,3,3,4,4,5,5,6]
num = int(input("Enter the number: "))
array  = SearchA(X, num)
n = len(array)

if(n == 0): print("Entered number not found", end="")

for i in range(n):
    print(array[i], end="")
    if i < n-1: print(",", end="")
print()