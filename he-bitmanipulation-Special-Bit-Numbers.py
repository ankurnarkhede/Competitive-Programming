def double_ones(num):
    flag = 0
    while (num):
        if (num % 2 == 1):
            flag += 1
            num //= 2

        elif (num % 2 == 0):
            flag = 0
            num //= 2

        if (flag == 2):
            return 1
    if (flag < 2):
        return 0

def main():
    n, q = map (int, input ().strip ().split (' '))
    a = list (map (int, input ().strip ().split (' ')))

    contains_one = []
    for i in range (0, n, +1):
        contains_one.append (double_ones (a[i]))

    for i in range (q):
        l, r = map (int, input ().strip ().split (' '))
        print (sum (contains_one[l - 1:r]))


if __name__ == '__main__':
    main()