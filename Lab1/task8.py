# Function
def SortedMerge(Arr1, Arr2):
    mergedArr = []
    for i in range(len(Arr1)):
        for j in range(len(Arr2)):
            if Arr1[i] <= Arr2[j]:
                mergedArr.append(Arr1[i])
                if i < len(Arr1) - 1:
                    if Arr1[i+1] > Arr2[j]:
                        mergedArr.append(Arr2[j])
                break
    if len(Arr1)>len(Arr2):
        greaterArr = Arr1 
    elif len(Arr1) != len(Arr2):
        greaterArr = Arr2
    for i in range(len(greaterArr)):
        if greaterArr[i] >= mergedArr[len(mergedArr)-1]:
            mergedArr.append(greaterArr[i])
    return mergedArr

# Driver
A = [0,3,4,10,11,13, 14 ,55, 100]
B = [1,8,13,24]

print(SortedMerge(A, B))