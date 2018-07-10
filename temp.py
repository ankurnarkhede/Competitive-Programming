# Write your code here

N = int (input ())

A = [int (x) for x in input ().strip ().split (' ')]


def inOrder(root, path):
    if root >= len (A):
        return
    inOrder (2 * root + 1, path)
    path.append (A[root])
    inOrder (2 * root + 2, path)


path = []
inOrder (0, path)

A.sort ()

M = {}
for i in range (len (A)):
    M[A[i]] = i

print(M)
print(path)
check = {}


def cycleSize(index):
    size = 1
    i = M[path[index]]
    check[i] = 1
    while i != index:
        i = M[path[i]]
        check[i] = 1
        size += 1
    return size


total = 0
for i in range (len (path)):
    if i not in check:
        total += cycleSize (i) - 1
        print(check)
print (total)