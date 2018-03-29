import sys
from collections import deque

q = int (sys.stdin.readline ().strip ())
queue = deque ([])
a = []

for i in range (0, q, +1):
    a = (list ((sys.stdin.readline ().strip ().split (' '))))
    if (len (a) > 1):
        queue.append (int (a[1]))
        print (len (queue))
    else:
        if queue:
            print (queue.popleft (), len (queue))
        else:
            print (-1, len (queue))
