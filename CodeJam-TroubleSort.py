def trouble_sort(a, l):
    done = False
    while not done:
        done = True
        for k in range(l-2):
            if a[k] > a[k+2]:
                done = False
                a[k], a[k+1], a[k+2] = a[k+2], a[k+1], a[k]
    return(a)

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    trouble_arr = trouble_sort(arr, n)
    if sorted(arr) == trouble_arr:
        print("Case #%d: OK"%(_+1))
    else:
        for i in range(n-1):
            if trouble_arr[i] > trouble_arr[i+1]:
                print("Case #%d:"%(_+1), i)
                break