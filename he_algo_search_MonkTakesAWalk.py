flag = 0

w = []

v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

n = int(input())
# print("count=",n)

for i in range(0, n, 1):
    c = 0
    w = input()

    len_w = len(w)
    for j in range(0, len_w, 1):
        # print('checking ',w[j])
        if (w[j] in v):
            c += 1
    print(c)
