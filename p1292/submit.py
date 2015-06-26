import math

a, b = map(int, raw_input().split())

print int(sum([round(math.sqrt(2*i)) for i in range(a, b+1)]))
