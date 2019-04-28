import math

c1 = [500, 300, 200, 50, 30, 10]
c2 = [512, 256, 128, 64, 32]

def rank1(r):
    if r < 1:
        return -1
    if r < 2:
        return 0
    if r < 4:
        return 1
    if r < 7:
        return 2
    if r < 11:
        return 3
    if r < 16:
        return 4
    if r < 22:
        return 5
    return -1

def rank2(r):
    if r < 1:
        return -1
    if r < 32:
        return int(math.log(r, 2))
    return -1

n = int(input())
s = []
for _ in range(n):
    a, b = map(int, input().split())
    ar, br = rank1(a), rank2(b)
    prize = 0
    if ar >= 0:
        prize += c1[ar]
    if br >= 0:
        prize += c2[br]
    s.append(prize*10000)

for e in s:
    print(e)
