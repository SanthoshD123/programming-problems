def max_of_minimums(arr, k):
    mini = []
    for i in range(len(arr)-k+1):
        minimum = min(arr[i:i+k])
        mini.append(minimum)
    return max(mini)


arr = [2, 5, 7, 8, 6]
k = 2
result = max_of_minimums(arr, k)
print("Maximum of the minimums is:", result)
