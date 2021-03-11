import sys


def main():
    t = int(sys.stdin.readline().strip())

    for i in range(0, t, +1):
        t = int(sys.stdin.readline().strip())

        a = (list(map(int, sys.stdin.readline().strip().split(' '))))
        index = 1
        days = 0
        while (index < len(a) - 1):
            people = sum(a[:index])
            index += people
            days += 1
        print(days)


if __name__ == "__main__":
    main()
