def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

arr = [12, 34, 54, 2, 3]
print("Array before sorting:")
for i in range(len(arr)):
    print(arr[i], end=" ")
shellSort(arr)
print("\nArray after sorting:")
for i in range(len(arr)):
    print(arr[i], end=" ")
