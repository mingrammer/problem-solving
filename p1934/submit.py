n = int(raw_input())
arr = []

def gcd(a, b):
    if a == 0: return b
    if b == 0: return a

    return gcd(a-b * (a/b), b) if a > b else gcd(a, b-a * (b/a))

for i in range(0, n):
    arr.append(map(int, raw_input().split()))

for i in range(0, n):
    a = arr[i][0]
    b = arr[i][1]
    
    print a * b / gcd(a, b)
