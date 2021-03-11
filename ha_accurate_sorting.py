#!/bin/python3

import math

q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    # Write Your Code Here

    x = a
    a_original = a
    a_sort = list(sorted(a))

    for i in range(0, n - 1, 1):
        if (math.fabs(x[i] - x[i + 1]) == 1.0):
            if (a[i] > a[i + 1]):
                temp = x[i]
                x[i] = x[i + 1]
                x[i + 1] = temp

    if (x == a_sort):
        print('Yes')
    else:
        print('No')
