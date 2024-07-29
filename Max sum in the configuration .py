def maxSum(arr, n):
    res = float('-inf')
    for i in range(n):
        curr_sum = 0
        for j in range(n):
            index = (i + j) % n
            curr_sum += j * arr[index]
        res = max(res, curr_sum)
    return res

arr = [8, 3, 1, 2]
print(maxSum(arr, len(arr)))  # Output: 29
