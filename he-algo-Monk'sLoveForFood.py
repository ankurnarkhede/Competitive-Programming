import sys

q = int(sys.stdin.readline().strip())
stack = []
a = []

for i in range(0, q, +1):
    a = list(map(int, sys.stdin.readline().strip().split(' ')))
    if (len(a) > 1):
        stack.append(a[1])
    else:
        if stack:
            print(stack.pop())
        else:
            print('No Food')
