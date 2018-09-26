# Longest Collatz sequence

n = 2
m, m_num = 1, 1
len_list = dict()


def get_collatz_len(k):
    m = 1
    while k > 1:
        if k % 2 == 0:
            k /= 2
            m += 1
        else:
            k = 3*k + 1
            m += 1
    return m

num_list = range(2, 1000000)

for num in num_list:
    callatz_len = get_collatz_len(num)
    if m < callatz_len:
        m = callatz_len
        m_num = num
print(m_num)
