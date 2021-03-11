n = int(input())
a = (list(map(int, input().strip().split(' '))))
k = int(input())
c = []
for i in range(0, 100002, 1):
    c.append(0)

# print(a)

for i in range(0, n, 1):
    var = a[i]
    c[var] += 1
# print(c)

for j in range(0, n, 1):
    # print(c[j])
    if (c[j] == k):
        print(j)
        break
