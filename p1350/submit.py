import math

input()
fs = map(float, raw_input().split())
cs = input()

print int(cs * sum(math.ceil(f / cs) for f in fs))
