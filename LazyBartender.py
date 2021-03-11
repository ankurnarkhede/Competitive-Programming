import operator

n = int(input())
c = int(input())

dict = {}

drinks = []

for i in range(c):
    a = (list(map(int, input().strip().split(' '))))

    drinks.append(a[1:])

    for j in range(1, len(a)):
        try:
            dict[a[j]] += 1

        except(KeyError):
            dict[a[j]] = 1

# print("drinks=", drinks)
# print("dict=", dict)

sorted_d = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
# print("SORTED=", sorted_d)

count = 0
deleted = True
while (deleted):
    deleted = False
    nos = sorted_d[0][0]
    del (sorted_d[0])
    for k in range(len(drinks)):
        if nos in drinks[k]:
            drinks[k] = [-1]
            deleted = True

    if (deleted):
        count += 1

    # print("DRINKS=", drinks, "count=", count)

print(count)
