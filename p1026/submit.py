import sys
r = lambda: sys.stdin.readline()
n = map(int, r().split())[0]

a_arr = map(int, (lambda: sys.stdin.readline())().split())
b_arr = map(int, (lambda: sys.stdin.readline())().split())

a_arr = sorted(a_arr)
b_arr = sorted(b_arr)[::-1]

sum = 0

for i in range(0, n):
    sum += a_arr[i] * b_arr[i]

print sum
