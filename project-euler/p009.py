# Special Pythagorean triplet

n = 500000
a, b, c = 0, 0, 0
left_divs = set()
div = 1
while div**2 <= n:
    if n % div == 0:
        left_divs.add(div)
    div += 1
for left_div in left_divs:
    a, b = 1000-left_div, 1000-n/left_div
    if a > 0 and b > 0:
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            break
print(a*b*c)
