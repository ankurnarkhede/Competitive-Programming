


import sys

t = int (input().strip())

for i in range (0, t, +1):
    n, k = (map (int, input().strip ().split (' ')))

    a = (list (map (int, input().strip ().split (' '))))

    a_sorted=sorted(a, reverse=True)
    threshold=a_sorted[k-1]

    qualified=sum(i >=threshold for i in a_sorted)

    print(qualified)
