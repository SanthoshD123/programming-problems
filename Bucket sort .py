def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >=0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(arr):
    max_value = max(arr)
    size = max_value/len(arr)
    
    # Create buckets and distribute the elements
    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        j = int(arr[i]/size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])
    
    # Sort the elements of each bucket
    for i in range(len(arr)):
        insertion_sort(buckets[i])
    
    # Concatenate the sorted buckets
    result = []
    for i in range(len(arr)):
        result += buckets[i]
    
    return result

# Example usage:
unsorted_array = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_array = bucket_sort(unsorted_array)
print("Sorted array is:", sorted_array)
