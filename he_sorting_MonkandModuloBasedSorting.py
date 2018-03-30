# n=len(array) and k= to be moded with
n, k = (map (int, input ().strip ().split (' ')))

# a=array
a = (list (map (int, input ().strip ().split (' '))))

arr = []
for i, j in enumerate (a):
    mod = j % k
    arr.append ((i, j, mod))
arr.sort (key=lambda x: x[0])
arr.sort (key=lambda x: x[2])
for i in arr:
    print (i[1], end=' ')
