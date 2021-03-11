import sys

n = int(sys.stdin.readline().strip())
qqq = list(map(int, sys.stdin.readline().strip().split()))
wwww = max(qqq)

mul = 1
r = 10 ** 5
while (wwww):
    qqq.sort(key=lambda x: (x / mul) % r)
    print(' '.join(map(str, qqq)))

    mul *= r
    wwww //= r
