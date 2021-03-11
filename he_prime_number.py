n = int(input("enter no."))

if (n >= 1):
    print(2, end=' ')

    for i in range(2, n + 1, 1):
        print("i=", i)

        for j in range(2, i, 1):
            print("j=", j)
            if (i % j == 0):
                print("divisible by", j)
                break

            if (j == i):
                print(i, end=' ')
