dictionary = {}
dictionary = \
    {
        'u': 'u',
        'l': 'l'
    }
print(dictionary)

for k in dictionary.keys():
    print(k)

for v in dictionary.values():
    print(v)

print(dictionary.keys())
print(dictionary.values())

dictionary['u'] = "m"
print(dictionary)
