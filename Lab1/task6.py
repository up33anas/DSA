# Function
def SumIterative(number):
    sum = 0
    while(number > 0):
        x = number%10
        number = int(number/10)
        sum += x
    return sum

def SumRecursive(number):
    if number <= 0: return 0
    return number%10 + SumRecursive(int(number/10))

# Driver
n = int(input())
print("Sum of digits is:", SumIterative(n))
print("Sum of digits is:", SumRecursive(n))