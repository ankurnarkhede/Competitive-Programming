from collections import Counter
import sys

def minDeletions(s: str) -> int:
    fDic = Counter(s)
    ans = 0
    counts = sorted(list(fDic.values()), reverse=True)
    for i in range(len(counts)):
        while counts[i] > 0 and counts.count(counts[i]) > 1:
            counts[i] -= 1
            ans += 1
    return ans


def main():
    str = sys.stdin.readline().strip()

    print(minDeletions(str))


if __name__ == "__main__":
    main()
