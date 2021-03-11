import sys


def trouble_fun(a, l):
    done = False
    while not done:
        done = True
        for k in range(l - 2):
            if a[k] > a[k + 2]:
                done = False
                a[k], a[k + 1], a[k + 2] = a[k + 2], a[k + 1], a[k]
    return (a)


for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    arr = trouble_fun(arr, n)
    if sorted(arr) == arr:
        print("Case #%d: OK" % (_ + 1))
    else:
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                print("Case #%d:" % (_ + 1), i)
                break
