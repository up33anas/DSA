def CountingSort(input):
    k = len(input)
    count = [0] * (k + 1)
    output = [0] * k
    m = max(input)

    for j in input:
        count[j] += 1

    for i in range(1, m + 1):
        count[i] += count[i - 1]

    for i in range(len(input) - 1, -1, -1):
        j = input[i]
        output[count[j] - 1] = j
        count[j] -= 1

    return output

arr = [2, 5, 3, 0, 2, 3, 0, 3]
ans = CountingSort(arr)
print(ans)