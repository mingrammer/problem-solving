m, n = map(int, raw_input().split())
print abs((m+3)/4-(n+3)/4) + abs((m+3)%4-(n+3)%4)
