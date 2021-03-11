import sys


def substring(str, min_length, ans):
    for i in range(len(str)):
        if (len(str[i:]) >= min_length):
            ans.append(str[i:])
        substring(str[i:i - 1], min_length, ans)
    return ans


def main():
    a = (sys.stdin.readline().strip())
    b = (sys.stdin.readline().strip())
    s = (sys.stdin.readline().strip())

    total = 0

    limit = max(len(a), len(b))
    ans = []
    arr = substring(s, limit, ans)
    print(arr)

    for i in range(0, len(arr), +1):
        if ((a in arr[i]) and (b in arr[i])):
            total += 1

    print(total)


if __name__ == "__main__":
    main()
