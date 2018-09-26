# Even Fibonacci numbers

m, n = 1, 2
fib = [m, n]
while n <= 4000000:
    m, n = n, m + n
    fib.append(n)
s = sum(f for f in fib if f % 2 == 0)
print (s)
