# 2
# 3 3 5 4
# 3 1 1 2
# 8
# 0 1
# 2
# 1 1 1
# 2
# 0 1
# 2
# 1 2 4
# 2


import sys
from collections import deque


n = int (sys.stdin.readline ().strip())
queue=deque([])

for i in range(0, n, +1):
    x = (list (map (int, sys.stdin.readline ().strip ().split (' '))))
    queue.append(x[1:])

    print('queue=',queue)

q = int (sys.stdin.readline ().strip())

for j in range(0, q, +1):
    str=(list (map (int, sys.stdin.readline ().strip ().split (' '))))

    # logic
    if(str[0]==0):
        index=str[1]-1
        popped=queue[index].pop()
        print(popped, ' this popped')

    if (str[0] == 1):
        index = str[1]-1
        queue[index].append(str[2])
        print(str[2],' added to queue')
        print('queue=', queue)

    if (str[0] == 2):
        pass

print ('final queue=', queue)





