def Minimum(Arr, starting, ending):
    newArr = Arr[starting : ending+1]
    min = newArr[0]
    for i in range(len(newArr)):
        if newArr[i] < min:
            min = newArr[i]
    for i in range(len(Arr) + 1):
        if Arr[i] == min: return i
        
def Sort4(Arr):
    newArr = []
    for i in range(len(Arr)):
        minIndex = Minimum(Arr, 0, len(Arr))
        min = Arr[minIndex]
        newArr.append(min)
        Arr.remove(min)
    return newArr

arr = [2, 3, 400 ,-9, 6, 5, 90, 0]
print(Sort4(arr))