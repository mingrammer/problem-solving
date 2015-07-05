def get_score(sym):
    if sym == 'A+': return 4.3
    if sym == 'A0': return 4.0
    if sym == 'A-': return 3.7
    if sym == 'B+': return 3.3
    if sym == 'B0': return 3.0
    if sym == 'B-': return 2.7
    if sym == 'C+': return 2.3
    if sym == 'C0': return 2.0
    if sym == 'C-': return 1.7
    if sym == 'D+': return 1.3
    if sym == 'D0': return 1.0
    if sym == 'D-': return 0.7
    if sym == 'F': return 0.0

m, a = 0, 0.0
for _ in range(input()):
    r = raw_input().split()
    n, s = r[1], r[2]
    m += int(n)
    a += get_score(s)*int(n)
print '%.2f ' % round(a/m+0.00001, 2)
