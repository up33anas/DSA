# Function
def ColumnWiseSum(Mat):
   
    sumArr = []
    for i in range(len(Mat[0])):
        sum = 0
        for j in range(len(Mat)):
            sum += Mat[j][i]
        sumArr.append(sum)
    return sumArr

def RowWiseSum(Mat) :
    sumArr = []
    for i in range(len(Mat)):
        sum = 0
        for j in range(len(Mat[0])):
            sum += Mat[i][j]
        sumArr.append(sum)
    return sumArr
        
# Driver
arr = [
    [1, 13, 13],
    [5, 11, 6],
    [4, 4, 9]
]
print("Column-wise:",ColumnWiseSum(arr))
print("Row-wise:",RowWiseSum(arr))