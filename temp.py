n = int (input ())
a = list (map (int, input ().split ()))
M = max (a) + 1
cnt = [0 for _ in range (M + 1)]
for el in a:
    cnt[el] += 1
print(cnt)

def gcd(a, b):
    if min (a, b) == 0:
        return max (a, b)
    return gcd (b, a % b)


dv = [0 for _ in range (M + 1)]

for num in range (1, M + 1):
    for nc in range (num, M + 1, num):
        dv[num] += cnt[nc]
print(dv)

for _ in range (int (input ())):
    p, q = map (int, input ().split ())
    g = gcd (p, q)
    print ((dv[p] if 0 < p <= M else 0) + (dv[q] if 0 < q <= M else 0) - (dv[p * q // g] if 0 < p * q // g <= M else 0))