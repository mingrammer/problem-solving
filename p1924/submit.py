import sys
x, y = map(int, (lambda : sys.stdin.readline())().split())


def enum(*sequencial, **named):
    enums = dict(zip(sequencial, range(len(sequencial))), *named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse'] = reverse
    return type('Enum', (), enums)


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = enum('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')

diff = y

for i in range(0, x-1): diff += days[i]

print weeks.reverse[diff % 7]
