from math import hypot

T = input()

cnts = [0 for _ in xrange(T)]

for i in xrange(T):
    x1,y1,x2,y2 = map(int, raw_input().split())

    for j in xrange(int(raw_input())):
        cx,cy,r = map(int, raw_input().split())

        if (hypot(cx-x1, cy-y1)-r)*(hypot(cx-x2, cy-y2)-r) < 0:
            cnts[i] += 1

for i in xrange(T):
    print cnts[i]
