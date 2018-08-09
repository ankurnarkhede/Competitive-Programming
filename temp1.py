def dist(i, j):
    c = 0
    while i != 0 and j != 0:
        i -= 1
        j -= 1
        c += 1
    if i == 0:
        if j == 0:
            return (c)
        else:
            return (c + j)
    else:
        return (c + i)


def is_poly(distances):
    _max = max (distances)
    _count = 0
    for i in distances:
        if i == _max:
            _count += 1

    return True if _count > 1 else False


def get_qualities(girls, i, j):
    row, col = len (girls), len (girls[0])
    quality = 0
    # Corner conditions
    if ((i > 0 and j > 0) and (girls[i - 1][j - 1] == 1)):
        quality += 1

    if ((i >= 0 and j > 0) and girls[i][j - 1] == 1):
        quality += 1

    if ((i < row - 1 and j > 0) and girls[i + 1][j - 1] == 1):
        quality += 1

    if ((i > 0 and j >= 0) and girls[i - 1][j] == 1):
        quality += 1

    if ((i < row - 1 and j >= 0) and girls[i + 1][j] == 1):
        quality += 1

    if ((i > 0 and j < col - 1) and girls[i - 1][j + 1] == 1):
        quality += 1

    if ((i >= 0 and j < col - 1) and girls[i][j + 1] == 1):
        quality += 1

    if ((i < row - 1 and j < col - 1) and girls[i + 1][j + 1] == 1):
        quality += 1

    return quality


def main():
    row, col = [int (i) for i in input ().strip ().split ()]
    girls = []
    qualities = [[0] * col] * row

    for i in range (0, row):
        girls.append ([int (i) for i in input ().strip ().split ()])

    girls[0][0] = 0

    qualities = []
    for i in range (0, row):
        for j in range (0, col):
            if girls[i][j] == 1:
                qualities.append ((get_qualities (girls, i, j), i, j))

    qualities = sorted (qualities, key=lambda x: x[0], reverse=True)
    # print ('qualities')
    # for i in qualities:
    #     print (i)

    if len (qualities) != 0:
        max_qualities = list (filter (lambda x: x[0] == qualities[0][0], qualities))

        # print ('max_qualities')
        # for i in max_qualities:
        #     print (i)

        if max_qualities[0][0] != 0:
            distances = []
            for i in max_qualities:
                distances.append (dist (i[1], i[2]))

            # print ('distances')
            # for i in distances:
                # print (i)

            if is_poly (distances):
                print ("Polygamy not allowed", end='')
            else:
                index = distances.index (min (distances))
                _ = max_qualities[index]
                print ('{}:{}:{}'.format (_[1] + 1, _[2] + 1, _[0]), end='')
        else:
            print ("No suitable girl found", end='')
    else:
        print ("No suitable girl found", end='')


if __name__ == "__main__":
    main ()
    # 6 6
    # 1 0 0 0 0 0
    # 0 0 0 0 0 0
    # 0 1 1 1 1 0
    # 0 1 1 1 1 0
    # 0 1 1 1 1 0
    # 0 0 0 0 0 0

    # 2 9
    # 1 0 1 1 0 1 1 1 1
    # 0 0 0 1 0 1 0 0 1