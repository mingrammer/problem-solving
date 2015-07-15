import math

T = input()

cnts = [0]*T

for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, raw_input().split())

    r = math.hypot(x1-x2, y1-y2)
    rs = r1+r2
    rd = abs(r1-r2)

    if r == 0: cnts[i] = -1 if rd == 0 else 0
    elif r < rd: cnts[i] = 0
    elif r == rd: cnts[i] = 1
    elif r < rs: cnts[i] = 2
    elif r == rs: cnts[i] = 1
    else: cnts[i] = 0

for c in cnts: print c
