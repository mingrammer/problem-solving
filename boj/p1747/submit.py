n = input()

def is_prime(k):
    d = 2
    if k < 2: return False
    while d**2 <= k:
        if k%d == 0: return False
        d += 1
    return True

while True:
    if is_prime(n):
        s = str(n)
        if s == s[::-1]: print n; break;
    n += 1
