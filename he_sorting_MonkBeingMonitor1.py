from collections import Counter

# Write your code here
T = int(input())

for i in range(T):
    l = []
    N = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    print(c)
    c = list(c.values())
    print(c)
    c.sort()
    print(c)
    if (c[-1] - c[0] > 0):
        print(c[-1] - c[0])
    else:
        print(-1)
