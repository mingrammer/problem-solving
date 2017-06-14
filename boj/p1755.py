m, n = map(int, raw_input().split())
r = 0
o = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
c = []

for e in range(m, n + 1):
    if e < 10:
        c.append(o[e])
    else:
        c.append(o[e / 10] + o[e % 10])

c.sort()
c = ' '.join(c)

for i in range(10):
    c = c.replace(o[i], str(i))

for e in c.split(" "):
    print e,
    r += 1
    if r % 10 == 0:
        print ''
