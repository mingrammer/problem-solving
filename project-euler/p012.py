# Highly divisible triangular number

n = 2
d = 2
cnt = 0
num = 1
primes = dict()
while True:
    m = n*(n+1)
    while d**2 <= m:
        while m % d == 0:
            m /= d
            cnt += 1
        primes[d] = cnt
        d += 1
        cnt = 0
    if m > 1:
        primes[m] = 1
    primes[2] -= 1
    for value in primes.values():
        num *= (value+1)
    if num >= 500:
        break
    n += 1
    d = 2
    num = 1
    primes.clear()
print(n*(n+1)/2)
