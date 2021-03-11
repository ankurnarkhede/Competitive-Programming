import sys

q = int(sys.stdin.readline().strip())
print('q=', q)

for i in range(0, q, +1):
    count = 0
    l, r = (map(int, sys.stdin.readline().strip().split(' ')))
    print('l=', l, ' r=', r)

    l_str, r_str = str(l), str(r)

    for j in range(l, r + 1, +1):
        print('================looking fr ', j)
        sum = 0
        flag = 1
        j_str = str(j)
        for k in range(0, len(str(j)), +1):
            sum += int(str(j_str[k])) * int(str(j_str[k]))
        print('sum=', sum)

        for m in range(0, len(str(j)), +1):
            print('checking fr', (int(str(j_str[m]))))
            if ((int(str(j_str[m])) != 0) and (sum % (int(str(j_str[m]))) != 0)):
                print('nahi hot')
                flag = 0

        if (flag):
            count += 1
            print('done for ', j)

    # print(count)
    print('count=', count)
