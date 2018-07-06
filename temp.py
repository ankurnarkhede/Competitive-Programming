

# 4,4
#
# 7,5,5,2
#
# 3,6,1,7
#
# 8,7,0,4
#
# 8,7,3,9
# 9743782557163078

# 2,3
#
# 1,2,3
#
# 2,4,6


import sys
from collections import deque


m,n= (map (int, sys.stdin.readline ().strip ().split (',')))
print(m,n)
ans=''
# chute=deque ()
chute=[]

for i in range(0,m,+1):
    chute.append(list (map (int, sys.stdin.readline ().strip ().split (','))))

print('chute=',chute)

high=[]

for j in range(0,n*n,+1):
    if(len(chute[j])>0):
        high.append(chute[j][-1])
    else:
        high.append(0)

max_num=max(high)
ans+=str(max_num)
del(chute[high.index(max_num)][-1])
print('modified chute=',chute)

print('current ans=',int(ans))



