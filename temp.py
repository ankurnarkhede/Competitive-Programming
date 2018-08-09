# 2 9
#
# 1 0 1 1 0 1 1 1 1
#
# 0 0 0 1 0 1 0 0 1


import sys
import math


def calc_dist(i, j):
    count = 0
    while i != 0 and j != 0:
        i -= 1
        j -= 1
        count += 1
    if i == 0:
        if j == 0:
            return (count)
        else:
            return (count + j)
    else:
        return (count + i)


def main():
    row, col = (map (int, sys.stdin.readline ().strip ().split (' ')))

    girls = []
    qualities = [[0 for i in range (col)] for j in range (row)]

    for i in range (0, row, +1):
        a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))
        girls.append (a)

    # print ("girls={}".format (girls))

    for i in range (0, row, +1):
        for j in range (0, col, +1):
            # print ("checking for", i, j)
            try:

                if (girls[i][j] == 1):

                    # to the left
                    if ((i > 0 and j > 0) and (girls[i - 1][j - 1] == 1)):
                        # print ("left up")
                        qualities[i][j] += 1

                    if ((i >= 0 and j > 0) and girls[i][j - 1] == 1):
                        # print ("left side")

                        qualities[i][j] += 1

                    if ((i < row - 1 and j > 0) and girls[i + 1][j - 1] == 1):
                        # print ("left down")

                        qualities[i][j] += 1

                    # middle line
                    if ((i > 0 and j >= 0) and girls[i - 1][j] == 1):
                        # print ("up")

                        qualities[i][j] += 1

                    if ((i < row - 1 and j >= 0) and girls[i + 1][j] == 1):
                        # print ("down")

                        qualities[i][j] += 1

                    # to the right
                    if ((i > 0 and j < col - 1) and girls[i - 1][j + 1] == 1):
                        # print ("right up")

                        qualities[i][j] += 1

                    if ((i >= 0 and j < col - 1) and girls[i][j + 1] == 1):
                        # print ("right")

                        qualities[i][j] += 1

                    if ((i < row - 1 and j < col - 1) and girls[i + 1][j + 1] == 1):
                        # print ("right down")

                        qualities[i][j] += 1
            except(Exception):
                continue

    print ("qualities={}".format (qualities))

    max_till_now = 0
    maximum = [0] * row
    max_row = [[0, 0]] * row
    count = 0
    for i in range (0, row, +1):
        if (max (qualities[i]) > max_till_now):
            maximum[count] = max (qualities[i])
            max_row[count] = [i, qualities[i].index (maximum[count])]
            count += 1

        elif (max (qualities[i]) == max_till_now):
            maximum[count] = max (qualities[i])
            max_row[count] = [i, qualities[i].index (maximum[count])]

    print (maximum, max_row)


    max1 = 0
    min_dist = sys.maxsize
    index = 0
    final_index=0
    for i in range (row):
        if (max (maximum) > max1):
            max1 = (max (maximum))
    print("max11=",max1)

    # find final index else find if its POLYGAMY
    polygamy=0
    min_count=0
    for i in range (0, col, +1):
        try:
            print("checking for ",maximum[i])
            if(maximum[i]==max1):
                print("max12=",max1)
                print("current polygamy=",polygamy)
                if (min_dist > calc_dist (max_row[index][0] + 1, max_row[index][1] + 1)):
                    polygamy=0
                    min_dist=calc_dist (max_row[index][0] + 1, max_row[index][1] + 1)
                    final_index=i
                elif(min_dist == calc_dist (max_row[index][0] + 1, max_row[index][1] + 1)):
                    polygamy=1
        except(Exception):
            continue


    print (max_row[final_index])


    # check if no girl found
    flag=0
    for i in range(0,row,+1):
        if(sum(girls[i])!=0):
            # girl found
            if(i==0 and sum(girls[i])==1):
                continue
            flag=1
            break

    # print final answer
    if(flag==1):
        if(polygamy==0):
            print ("{}:{}:{}".format (max_row[final_index][0] + 1, max_row[final_index][1] + 1, max1), end='')
        elif(polygamy==1):
            print ("Polygamy not allowed", end='')
    elif(flag==0):
        print("No suitable girl found", end='')



if __name__ == "__main__":
    main ()
