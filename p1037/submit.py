import sys

r = lambda: sys.stdin.readline()
n = int(r().split()[0])

divisor_set = map(int, (lambda: sys.stdin.readline())().split())
divisor_set = sorted(divisor_set)

num = 1

if len(divisor_set) == 1:
    num = divisor_set[0] * divisor_set[0]
else:
    num = divisor_set[0] * divisor_set[-1]

print num
