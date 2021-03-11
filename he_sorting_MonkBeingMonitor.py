# choose 2 students having heights h1 and h2 respectively,
# such that h1>h2 and difference between the
#  number of students having height h1 and number of students having height h2 is maximum.

import sys
from collections import Counter

for i in range(0, int(sys.stdin.readline()), +1):
    n = int(sys.stdin.readline())
    a = (list(map(int, sys.stdin.readline().strip().split(' '))))

    # logic s

    c = Counter(a)
    c = list(c.values())
    c.sort()

    print(c[-1] - c[0]) if c[-1] - c[0] > 0 else print(-1)

    # logic e
