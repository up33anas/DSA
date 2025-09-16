def Minimum(Arr, starting, ending):
    newArr = Arr[starting : ending+1]
    min = newArr[0]
    for i in range(len(newArr)):
        if newArr[i] < min:
            min = newArr[i]
    for i in range(len(Arr) + 1):
        if Arr[i] == min: return i
        
def Sort4(arr):
    arr = arr[:]
    newArr = []
    while arr:
        minIndex = Minimum(arr, 0, len(arr))
        newArr.append(arr[minIndex])
        arr.pop(minIndex)
    return newArr

def Sort10(Arr):
    positiveArr = []
    negativeArr = []
    newArr = []
    for i in range(len(Arr)):
        if Arr[i] >= 0:
            positiveArr.append(Arr[i])
        else: negativeArr.append(Arr[i])
    positiveArr = Sort4(positiveArr)
    negativeArr = Sort4(negativeArr)

    maxLen = len(negativeArr) if len(negativeArr) > len(positiveArr) else len(positiveArr)
    for i in range(maxLen):
        if i < len(negativeArr):
            newArr.append(negativeArr[i])
        if i < len(positiveArr):
            newArr.append(positiveArr[i])
    return newArr

arr = [10, -1, 9, 20, -3, -8, 22, 9, 7]
print(Sort10(arr))