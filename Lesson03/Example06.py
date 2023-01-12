d = [x for x in range(10)]
res = list(filter(lambda x: not x%2, d))
print(res)

users = ['u1','u2','u3','u4','u5']
ids = [4,5,9,14,7]

data = list(zip(users, ids))
print(data)

salary = [111,222,333]
data = list(zip(users, ids,salary))
print(data)

n_users = list(enumerate(users))
print(n_users)
