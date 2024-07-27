def woodCollected(height, n, m):
	sum = 0
	for i in range(n - 1, -1, -1):
		if (height[i] - m <= 0):
			break
		sum += (height[i] - m)

	return sum
def collectKWood(height, n, k):
	height = sorted(height)
	low = 0
	high = height[n - 1]
	while (low <= high):
		mid = low + ((high - low) // 2)
		collected = woodCollected(height, n, mid)
		if (collected == k):
			return mid
		if (collected > k):
			low = mid + 1
		else:
			high = mid - 1
	return -1
height = [1, 2, 1, 2]
n = len(height)
k = 2
print(collectKWood(height, n, k))
