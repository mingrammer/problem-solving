# Multiples of 3 and 5

n = 1000
s = sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
print(s)
