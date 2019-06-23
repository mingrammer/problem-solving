for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1,n):
            t = a[n*i + j]
            a[n*i + j] = a[j*n + i]
            a[j*n + i] = t
    for i in range(n):
        for j in range(n//2):
            t = a[n*i + j]
            a[n*i + j] = a[n*i+(n-1-j)]
            a[n*i + (n-1-j)] = t
    print(' '.join(map(str, a)))

