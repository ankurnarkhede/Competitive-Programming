# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/
# 1
# 4

import sys


def count_set_bits(n):
    set_bits = 0
    while (n > 0):
        set_bits += n & 1
        n >>= 1
    return set_bits


def main():
    t = int(sys.stdin.readline().strip())

    for i in range(0, t, +1):
        n = int(sys.stdin.readline().strip())
        print(count_set_bits(n))


if __name__ == "__main__":
    main()
