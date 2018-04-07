


def trouble_fun(a, l):
    done = False
    while not done:
        done = True
        for k in range(l-2):
            if a[k] > a[k+2]:
                done = False
                a[k], a[k+2] = a[k+2], a[k]
    return(a)

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    arr = trouble_fun(arr, n)
    flag=False
    for i in range(0, n-1, +1):
        if(arr[i+1]<arr[i]):
            print("Case #%d:"%(_+1), i)
            flag=True
    if not flag:
        print("Case #%d: OK"%(_+1))

