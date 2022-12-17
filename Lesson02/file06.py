def concatination(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatination('a','b','c'))
print(concatination('a','1'))

