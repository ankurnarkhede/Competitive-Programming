

import sys

def main():

    semi_primes=[6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155, 158, 159, 161, 166, 177, 178, 183, 185, 187, 194]

    t= int (sys.stdin.readline ().strip())

    for i in range (0, t, +1):
        n = int (sys.stdin.readline ().strip ())
        flag=0

        for j in range(0, len(semi_primes), +1):
            for k in range (j, len (semi_primes), +1):
                if(semi_primes[j]+semi_primes[k]==n):
                    flag=1
                    break
            if(flag):
                break

        print("YES") if flag else print("NO")


if __name__ == "__main__":
    main ()