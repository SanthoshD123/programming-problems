def counting_sort(arr):
    # Find the maximum element in the array to determine the range of values
    max_val = max(arr)
    size = len(arr)
    count = [0] * (max_val + 1)
    output = [0] * size

    # Count each element
    for num in arr:
        count[num] += 1

    # Calculate cumulative count
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # Place the elements in the sorted order
    for i in range(size - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    # Copy the sorted elements into the original array
    for i in range(size):
        arr[i] = output[i]

    return arr

# Example usage:
unsorted_array = [1, 4, 1, 2, 7, 5, 2]
sorted_array = counting_sort(unsorted_array)
print("Sorted Array:", sorted_array)
