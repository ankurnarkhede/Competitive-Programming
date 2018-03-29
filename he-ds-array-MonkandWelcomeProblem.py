

import sys

n = int (sys.stdin.readline ())
a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))
b = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

sum=[]

for i in range(n):
    sum.append(a[i]+b[i])
print(*sum)