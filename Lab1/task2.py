from funcs import SearchB

# Driver
if __name__ == "__main__":
    X = [1,2,2,5,7,9,11,13,22]
    num = int(input("Enter the number: "))
    array  = SearchB(X, num)
    n = len(array)

    if(n == 0): print("Entered number not found", end="")

    for i in range(n):
        print(array[i], end="")
        if i < n-1: print(",", end="")
    print()