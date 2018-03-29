import sys
from collections import deque

q = int (sys.stdin.readline ())
monk_queue = deque ([])
x, y = 0, 0

for i in range (0, q, +1):
    # print (i, '=========================\nq=', monk_queue)

    ip = (sys.stdin.readline ().strip ().split (' '))
    if (len (ip) == 3):
        char, x, y = ip[0], ip[1], ip[2]
    elif (len (ip) == 1):
        char = ip[0]

    if (char == 'E'):
        flag_e = 0
        x, y = int (x), int (y)
        for j in range (len (monk_queue), 0, -1):
            if (monk_queue[j - 1][0] == x):
                monk_queue.insert (j, [x, y])
                flag_e = 1
                break
        if (flag_e == 0):
            monk_queue.append ([x, y])

    elif (char == 'D'):
        popped=monk_queue.popleft ()
        print (*popped)
