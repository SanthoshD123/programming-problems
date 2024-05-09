n = 153
temp = n
result = 0

while temp > 0:
    digit = temp % 10
    result += digit ** 3
    temp //= 10

if result == n:
    print("It's an Armstrong number:", n)
else:
    print("It's not an Armstrong number:", n)
