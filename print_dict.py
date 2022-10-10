dico = {'name': 'a', 'age': 3, 'id': 4444}

for items in sorted(dico):
    print("{}: {}".format(items, dico.get(items)))

n = list(dico)

print(n.sort)

