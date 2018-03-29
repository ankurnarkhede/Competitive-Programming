import sys


def index_search(a, target, length):
    low, high = 0, length
    if a[length] == target:
        return length
    while low < high:
        mid = (high + low) >> 1
        if a[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


arr, add = [], [0]

n, q = (map (int, sys.stdin.readline ().strip ().split (' ')))
for i in range (0, n, +1):
    l, r = (map (int, sys.stdin.readline ().strip ().split (' ')))
    arr.append ((l, r))
    #   creating (l,r) array of inputs
    add.append (add[i] + (r - l + 1))
# creating array of offsets

for j in range (0, q, +1):
    # reading the input x
    x = int (sys.stdin.readline ())
    # findinf the index in add list  after which, the target is present
    index = index_search (add, x, n)
    arr_index = x - add[index - 1] - 1
    print (arr[index - 1][0] + arr_index)
