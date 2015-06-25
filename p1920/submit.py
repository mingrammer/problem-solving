import sys

n = int(raw_input())
n_arr = set(map(int, raw_input().split()))
m = int(raw_input())
m_arr = map(int, raw_input().split())

for i in range(0, m):
    print 1 if m_arr[i] in n_arr else 0
