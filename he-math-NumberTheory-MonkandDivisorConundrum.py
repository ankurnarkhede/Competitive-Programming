import sys


def gcd(x, y):
    # cpmpute gcd using euclid's method
    while y != 0:
        (x, y) = (y, x % y)
    return x


def lcm(x, y):
    """This function takes two integers and returns the L.C.M."""
    return (x * y) // gcd(x, y)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    max1 = max(a) + 1
    ifindex = [0 for _ in range(max1 + 1)]

    # mark index if present in array
    for i in a:
        ifindex[i] += 1

    # list of number of multiples in given index for the list
    multiples = [0 for _ in range(max1 + 1)]
    for num in range(1, max1 + 1):
        for nc in range(num, max1 + 1, num):
            multiples[num] += ifindex[nc]

    for _ in range(int(sys.stdin.readline().strip())):
        p, q = (map(int, sys.stdin.readline().strip().split(' ')))

        # taking count by n(p)+n(q)-n(lcm(p,q))
        print((multiples[p] if 0 < p <= max1 else 0) + (multiples[q] if 0 < q <= max1 else 0) - (
            multiples[lcm(p, q)] if 0 < lcm(p, q) <= max1 else 0))
