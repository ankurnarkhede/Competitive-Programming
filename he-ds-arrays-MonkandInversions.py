for x in range(int(input())):
    n = int(input())
    m, l = [], []
    invert = 0
    for y in range(n): m.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            l.append((i, j))

    for i, j in l:
        for element in (map(lambda x: m[x[0]][x[1]], list(filter(lambda t: t[0] >= i and t[1] >= j, l)))):
            if m[i][j] > element: invert += 1

    print(invert)
