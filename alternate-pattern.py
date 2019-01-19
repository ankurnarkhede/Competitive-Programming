import math


def star_hash(i, j):
    print('*' * i + '#' * j)
    return True


def hash_star(i, j):
    print('#' * i + '*' * j)
    return True


n = int(input())
mid = math.ceil(n / 2)

for k in range(1, n + 1):
    if (k <= mid):
        if (k % 2):
            star_hash(k, n - k)
        else:
            hash_star(n - k, k)
    else:
        if (k % 2):
            star_hash(n - k + 1, n - (n - k) - 1)
        else:
            hash_star(n - (n - k) - 1, n - k + 1)
