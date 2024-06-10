def merge(arr, left, mid, right):
    # Create temporary arrays to hold the two halves
    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]
    
    # Initial indexes for the left, right and merged array
    left_index = 0
    right_index = 0
    merge_index = left
    
    # Merge the two halves back into the original array
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            arr[merge_index] = left_half[left_index]
            left_index += 1
        else:
            arr[merge_index] = right_half[right_index]
            right_index += 1
        merge_index += 1
    
    # Copy any remaining elements of the left half
    while left_index < len(left_half):
        arr[merge_index] = left_half[left_index]
        left_index += 1
        merge_index += 1
    
    # Copy any remaining elements of the right half
    while right_index < len(right_half):
        arr[merge_index] = right_half[right_index]
        right_index += 1
        merge_index += 1

def merge_sort(arr):
    current_size = 1
    
    # Iteratively merge subarrays in bottom up manner.
    # First merge subarrays of size 1 to create sorted subarrays of size 2, then merge subarrays of size 2 to create sorted subarrays of size 4, and so on.
    while current_size < len(arr) - 1:
        left_start = 0
        
        while left_start < len(arr) - 1:
            # Find the mid and right indices
            mid = min(left_start + current_size - 1, len(arr) - 1)
            right_end = min(left_start + 2 * current_size - 1, len(arr) - 1)
            
            # Merge the two halves
            merge(arr, left_start, mid, right_end)
            left_start += 2 * current_size
        
        # Double the size for the next iteration
        current_size = 2 * current_size

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array is:", arr)
