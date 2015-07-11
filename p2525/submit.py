h, m = map(int, raw_input().split())
t = input()
e = 60*h + m + t
print e/60 if e < 24*60 else e/60-24,; e -= (e/60)*60
print e
