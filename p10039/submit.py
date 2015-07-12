s = [0]*5
for _ in range(5):
    p = input()
    if p<40: p=40
    s.append(p)
print sum(s)/5
