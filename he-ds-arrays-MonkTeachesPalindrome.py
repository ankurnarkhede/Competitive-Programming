import sys

n = int (sys.stdin.readline ())

for i in range(0, n, +1):
    str=sys.stdin.readline ()
    reverse=''.join(reversed(str))

    if(str==reverse):
        if(len(str)%2==0):
            print('YES EVEN')
        else:
            print ('YES ODD')
    else:
        print('NO')