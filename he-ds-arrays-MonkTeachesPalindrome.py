import sys

n = int(sys.stdin.readline().strip())

for i in range(0, n, +1):
    str = (sys.stdin.readline().strip())

    if (str == "".join(list(reversed(str)))):
        if (len(str) % 2 == 0):
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')
