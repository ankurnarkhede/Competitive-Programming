import sys


def main():
    cases = int (sys.stdin.readline ())
    for case in range (cases):
        n, k, v = [int (a) for a in sys.stdin.readline ().split ()]
        l = []
        for _ in range (n):
            l.append (sys.stdin.readline ().strip ())
        ns = range (k * (v - 1), k * v)
        ns = [i % n for i in ns]
        ns = sorted (ns)
        ans = [l[i] for i in ns]
        ans = ' '.join (ans)
        print ('Case #{}: {}'.format (case + 1, ans))


main ()