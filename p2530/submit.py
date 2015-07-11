h, m, s = map(int, raw_input().split())
t = input()
e = 3600*h + 60*m + s + t
print e/3600 if e < 24*60*60 else e/3600 - ((e/3600)/24)*24,; e -= (e/3600)*3600
print e/60,; e -= (e/60)*60
print e
