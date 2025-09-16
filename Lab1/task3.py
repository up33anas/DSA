# Function
def Minimum(Arr, starting, ending):
    newArr = Arr[starting : ending+1]
    min = newArr[0]
    for i in range(len(newArr)):
        if newArr[i] < min:
            min = newArr[i]
    for i in range(len(Arr) + 1):
        if Arr[i] == min: return i

# Driver
array= [1, 2, 3, 4, -1]
print(Minimum(array,1,4))