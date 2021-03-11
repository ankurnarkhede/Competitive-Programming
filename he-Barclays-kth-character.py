s = input()
set_s = list(set(s))
# print(set_s)

new = []

for i in set_s:
    new.append("".join(list(filter(lambda a: a != i, s))))
    # print(new)
print(sorted(new)[0])
