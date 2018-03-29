# SAMPLE INPUT
#
# 2
# 6
# 5 3 1 4 3 2
# 4 3 1 1 1 5
# 5
# 1 2 3 4 5
# 5 4 3 2 1

rupam = []
ankit = []
r = 0
a = 0
t = int (input ())

for i in range (0, t, 1):
    r = 0
    a = 0
    n = int (input ())
    rupam = (list (map (int, input ().strip ().split (' '))))
    # print(rupam)
    r = sum (rupam)

    ankit = (list (map (int, input ().strip ().split (' '))))
    a = sum (ankit)
    # print(ankit)

    # result
    if (r > a):
        print ('Rupam')
    elif (r < a):
        print ('Ankit')
    else:
        print ('Tie')