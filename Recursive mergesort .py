def merge_sort(arr):
    # Base case: if the array is empty or contains a single element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index to divide the array into two halves
    mid = len(arr) // 2

    # Recursively sort the left and right halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Compare elements from left and right arrays and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in the left array, add them to the merged array
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # If there are remaining elements in the right array, add them to the merged array
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Example usage:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
