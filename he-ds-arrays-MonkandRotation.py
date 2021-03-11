import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for i in range(0, t, +1):
    n, k = (map(int, sys.stdin.readline().strip().split(' ')))
    arr = deque(list(map(int, sys.stdin.readline().strip().split(' '))))
    to_rotate = k % n
    arr.rotate(to_rotate)
    print(*arr)
