m = 'ABCDEFGHIJKLMNO'
o = ['ABCD', 'EFGH', 'IJKL', 'MNO.']
p = [raw_input() for _ in range(4)]
s = 0
def find(l, f):
    for i, e in enumerate(l):
        try: j = e.index(f); break
        except ValueError: pass
    return i, j
for e in m:
    a = find(o, e)
    b = find(p, e)
    s += abs(a[0]-b[0]) + abs(a[1]-b[1])
print s
