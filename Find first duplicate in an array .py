def first_repeating_element(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return arr[i]
    return None
my_array = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating_element(my_array)
print(f"First repeating element is {result}")
