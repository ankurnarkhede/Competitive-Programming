# 1
# 5 10
# 8 5 4 3 2

import sys

t= int (sys.stdin.readline ())

for i in range(t):
    n, x = (map (int, sys.stdin.readline ().strip ().split (' ')))
    a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

    a=sorted(a)
    capacity=int(x)
    count=0

    for j in range(0,n,+1):
        if(a[j]>capacity):
            break

        if(a[j]<capacity):
            capacity-=a[j]
            count+=1

    print('Count={}'.format(count))
    print(count)


