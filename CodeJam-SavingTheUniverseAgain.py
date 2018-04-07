

import sys

def damage(ip_str):
    dam=0
    power=1
    for i in ip_str:
        if(i=='C'):
            power*=2
        if(i=='S'):
            dam+=power
    return dam


n = int (sys.stdin.readline ().strip ())

for i in range(0,n,+1):

    d, ip_str =  sys.stdin.readline ().strip ().split (' ')
    d=int(d)
    ip_str=list(ip_str)

    # logic

    attempts=0
    while(d<damage(ip_str)):
        flag=False
        for j in range(len(ip_str)-1, 0, -1):
            if(ip_str[j]=='S' and ip_str[j-1]=='C'):
                ip_str[j], ip_str[j-1]=ip_str[j-1], ip_str[j]
                attempts+=1
                flag=True
                break
        if not flag:
            print('Case #{}: IMPOSSIBLE'.format(i+1))
            break

    if d>=damage(ip_str):
        print('Case #{}: {}'.format(i+1, attempts))


















