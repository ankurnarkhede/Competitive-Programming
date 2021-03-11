import math

n = int(input())
b = 1
half = n // 2
while b <= half:
    X = 2 * n - b * b - b
    if X < 0:
        print("NO")
        break

    a = (-1 + math.sqrt(1 + 4 * X)) / 2
    if int(a) != a:
        b += 1
        continue

    print("YES")
    break
