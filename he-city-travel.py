# https://www.hackerearth.com/challenge/competitive/september-circuits-18/algorithm/city-travel-59bad87f/

# 21 5 2
# 2 4
# 4 8

import sys


def main():
    dict = {}
    s, x, n = (map(int, sys.stdin.readline().strip().split(' ')))

    for i in range(n):
        t, y = (map(int, sys.stdin.readline().strip().split(' ')))
        dict[t] = y

    day = 0
    while (s > 0):
        if (dict.get(day, 0)):
            s -= dict.get(day)
        else:
            s -= x
        day += 1

    print(day)


if __name__ == "__main__":
    main()
