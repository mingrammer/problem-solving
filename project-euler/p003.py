# Largest prime factor

n = 600851475143
d = 2
primes = set()
while d**2 <= n:
    while n % d == 0:
        n /= d
        primes.add(d)
    d += 1
if n > 1:
    primes.add(n)
print(max(primes))
