# Summation of primes

m = 2000000
num, div = 2, 1
is_prime = True
sum_prime = 0
while num < m:
    div = 1
    is_prime = True
    while div**2 <= num:
        div += 1
        if div < num and num % div == 0:
            is_prime = False
            break
    if is_prime:
        sum_prime += num
    num += 1
print(sum_prime)
