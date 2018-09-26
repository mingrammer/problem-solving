# Smallest multiple

n, c = 1, 0
primes = [2, 3, 5, 7, 11, 13, 17, 19]
for p in primes:
    c = 0
    while p**(c+1) <= 20:
        c += 1
    n *= (p**c)
print(n)
