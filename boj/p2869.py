import math
a, b, v = map(int, raw_input().split())
print int(math.ceil(float(v-a)/(a-b)))+1
