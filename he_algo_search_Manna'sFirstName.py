# Input Format
# The first line contains the number of testcases, T. Next, T lines follow each containing a long string S.
#
# Output Format
# For each long string S, display the no. of times SUVO and SUVOJIT appears in it.

# SUVO = 0, SUVOJIT = 1
# SUVO = 1, SUVOJIT = 0


w = []
n = int(input())

for i in range(0, n, 1):
    w = input()
    s1 = w.count("SUVO")
    s2 = w.count("SUVOJIT")
    s1 = s1 - s2
    print('SUVO = ', s1, ', SUVOJIT = ', s2, sep='')
