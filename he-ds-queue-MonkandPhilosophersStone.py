import sys
from collections import deque

monk_queue = deque ([])
count = 0


def check_worth(queue, c):
    if (sum (queue) == x):
        print (len (queue))
        c = c + 1
        return c
    else:
        return c


n = int (sys.stdin.readline ().strip ())
worth = deque (list (map (int, sys.stdin.readline ().strip ().split (' '))))
q, x = (map (int, sys.stdin.readline ().strip ().split (' ')))

for i in range (0, q, +1):
    query = (sys.stdin.readline ().strip ())
    if (query == "Harry"):
        monk_queue.append (worth.popleft ())
        count = check_worth (monk_queue, count)
    elif (query == "Remove"):
        monk_queue.pop ()

if not count:
    print (-1)
