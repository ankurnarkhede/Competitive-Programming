import sys


def solution(a, b):
    # find k such that k>0 and (a * k) % b ** c == 0

    for j in range(141813280, sys.maxsize):
        print('j=', j)
        if ((a * j) % (b ** c) == 0):
            return j


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    for i in range(0, n, +1):
        a, b, c = (map(int, sys.stdin.readline().strip().split(' ')))

        print(solution(a, b))
