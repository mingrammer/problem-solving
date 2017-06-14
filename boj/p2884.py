h ,m = map(int, raw_input().split())
t = h*60 + m - 45
if t > 0: print t / 60, t % 60
else: print t / 60 + 24, t % 60
