
import sys

def getAns(n,m):
    flag = 0
    start=int(n**0.5)
    end=m//2
    for j in range (start, end+1, +1):
        temp = j % m
        if ((temp * temp) % m == n):
            flag = 1
            break

    if flag:
        return j
    return -1


if __name__ == "__main__":
    for i in range (0, int (sys.stdin.readline ().strip ()), +1):
        n, m = (map (int, sys.stdin.readline ().strip ().split (' ')))
        print(getAns(n,m))