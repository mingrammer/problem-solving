n = int(raw_input())

c_n = (n % 10) * 10 + ((n % 10 + n / 10) % 10)
count = 1

while c_n != n:
    c_n = (c_n % 10) * 10 + ((c_n % 10 + c_n / 10) % 10)
    count += 1

print count
