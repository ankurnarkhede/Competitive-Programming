import sys

from collections import deque

n = int(sys.stdin.readline().strip())

d = deque([1, 2, 3, 4, 5])

for i in range(0, n, +1):
    str = (sys.stdin.readline().strip())

n = int(input())
n = int(sys.stdin.readline())

a = (list(map(int, input().strip().split(' '))))

a = (list(map(int, sys.stdin.readline().strip().split(' '))))

#    print ((str (ser[k])).zfill (5), end=' ')

n, k = (map(int, sys.stdin.readline().strip().split(' ')))

n, k = (map(int, input().strip().split(' ')))

string, k = (map(str, input().strip().split(' ')))

a = [int(input()) for b in (range(n))]
arr = [int(x) for x in sys.stdin.readline().split()]

# initialize dictionary
dict = {}

ans = []
for i, j in enumerate(a):
    q = j % k
    ans.append((i, j, q))
ans.sort(key=lambda x: x[0])
ans.sort(key=lambda x: x[2])
for i in ans:
    # print (i[1], end=' ', sep='' )

    def most_common(lst):
        return max(set(lst), key=lst.count)

import sys


def main():
    n = int(sys.stdin.readline().strip())

    for i in range(0, n, +1):
        a = (list(map(int, sys.stdin.readline().strip().split(' '))))

        n, k = (map(int, sys.stdin.readline().strip().split(' ')))


if __name__ == "__main__":
    main()
