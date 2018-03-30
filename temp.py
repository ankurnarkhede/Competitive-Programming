# ip
# 4 8
# 1 2 3 4

import sys

n, x = (map (int, sys.stdin.readline ().strip ().split (' ')))
a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))
k=0

for i in range(0,n,+1):
    print(i,'=======================')
    sub_array=[]
    sub_array_sum=[]
    for j in range (0, n-i, +1):
        # sub_array.append(a[j:j+i+1])
        # print(sub_array)

        # sub_array.append(a[j:j+i+1])
        sub_array_sum.append (sum(a[j:j+i+1]))
        # print(sub_array_sum)

    # print(max(sub_array_sum))
    if(max(sub_array_sum)<=x):
        k+=1
        # print('k=',k)

print(k)






