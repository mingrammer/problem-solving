import sys

def main():
    n, m = map(int, (lambda: sys.stdin.readline())().split())

    print abs(n-m)

if __name__ == '__main__':
    main()
