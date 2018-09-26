# 10001st prime

idx, cnt = 10001, 0
num, div = 2, 1
is_prime = True
while cnt < idx:
    div = 1
    is_prime = True
    while div**2 <= num:
        div += 1
        if div < num and num % div == 0:
            is_prime = False
            break
    if is_prime:
        cnt += 1
    if cnt == idx:
        break
    num += 1
print(num)
