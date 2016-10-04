def fibonacci(n):
    a, b = 1, 1

    for i in range(n - 2):
        a, b = b, a + b

    return b

n = int(input())

print(2 * fibonacci(n + 2))
