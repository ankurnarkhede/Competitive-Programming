import sys

q = int (sys.stdin.readline ())
que = []
q1 = [[], [], [], []]
for _ in range (q):
    s = list (sys.stdin.readline ().split ())
    if len (s) > 1:
        t = int (s[1])
        u = int (s[2])
        if t not in que:
            que.append (t)
        q1[t - 1].append (u)

    else:
        print (que[0], q1[que[0] - 1].pop (0))
        if len (q1[que[0] - 1]) == 0:
            que.pop (0)
