def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            print(p)

# Example usage
num = 30
print("Following are the prime numbers smaller than or equal to", num)
sieve_of_eratosthenes(num)
