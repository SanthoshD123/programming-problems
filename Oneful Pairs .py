def is_oneful_pair(a, b):
    return a + b + (a * b) == 111

# Input
a, b = map(int, input().split())

# Check if (a, b) is a Oneful Pair
if is_oneful_pair(a, b):
    print("Yes")
else:
    print("No")
