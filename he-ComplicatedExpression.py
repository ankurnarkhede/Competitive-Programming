import sys

m = []
index = 0


def a(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(factors)


x, n = (map(int, sys.stdin.readline().strip().split(' ')))
arr = (list(map(int, sys.stdin.readline().strip().split(' '))))
fact = []
for i in range(0, len(arr), +1):
    fact.append(a(arr[i]))
# print('fact=',fact)
step = n - x + 1
j = 0
for j in range(j, j + step, +1):
    # print ('j=', j, ' step+j=', step + j)
    maxx = max(fact[j:j + step])
    for x in range(j + step - 1, j - 1, -1):
        # print('x=',x)
        if (fact[x] == maxx):
            index = x
            break
    # print('index=',index)
    m.append(arr[index])

# print('ans=',m)
print(min(m))
