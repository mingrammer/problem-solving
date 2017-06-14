from fractions import gcd

m, n = map(int, raw_input().split())

print m + n - gcd(m,n)
