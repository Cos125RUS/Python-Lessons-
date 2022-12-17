a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 21}
c = a.copy()
print(c)
u = a.union(b)
print(u)
i = a.intersection(b)
print(i)
dl = a.difference(b)
dr = b.difference(a)
print(dl)
print(dr)

q = a\
    .union(b) \
    .difference(a.intersection(b))

print(q)
