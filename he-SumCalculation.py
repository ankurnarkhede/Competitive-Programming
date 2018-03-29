import sys
from math import floor

t = int (sys.stdin.readline ().strip ())
print (t)
for x in range (0, t, +1):
    sum = 0
    n = int (sys.stdin.readline ().strip ())
    print (n)
    a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))
    a = sorted (a)
    length = len (a)
    for j in range (0, n, +1):
        for i in range (0, length, +1):
            sum += floor (a[i] / a[j])
            # sum +=  (a[i] % a[j])
    print (sum)
