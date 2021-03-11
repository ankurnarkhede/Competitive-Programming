# Little Monk and his toy-story
# https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/little-monk-and-his-toy-story/

# 4
# 40 100 20 30


import sys


def main():
    n = int(sys.stdin.readline())
    w = (list(map(int, sys.stdin.readline().strip().split(' '))))

    w.sort()
    total = 0
    count = 0
    i = 0

    while (i <= len(w) and total <= n):
        i += (1)
        total += i
        if (total <= n):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
