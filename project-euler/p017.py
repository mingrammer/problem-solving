# Number letter counts

one_digit = [3, 3, 5, 4, 4, 3, 5, 5, 4]
ten_to_twenty = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
two_digit = [6, 6, 5, 5, 5, 7, 6, 6]

hundred = 7
thousand = 8
and_letter = 3

sum_len = 0

sum_len += sum(one_digit)
sum_len += sum(ten_to_twenty)
sum_len += 10*sum(two_digit) + 8*sum(one_digit)
sum_len += 100*sum(one_digit) + 900*hundred + 9*99*and_letter + 9*(sum(ten_to_twenty) + 10*sum(two_digit) + 9*sum(one_digit))
sum_len += thousand + one_digit[0]

print(sum_len)
