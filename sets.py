'''
set is like a math sets

it has unique values. Different data types or value that are never repeated
set is just like dictionary but we only have values

it can contain many data types
'''

nlist = [1, 2, 3, 4, 5]
print(nlist)
nset = set(nlist)
print(nset)
nset.add(6)
print(nset)

cset = {6, 7, 3, 9}

uni = nset.union(cset)
print(uni)

intersec = nset.intersection(cset)
print(intersec)
diff = nset.difference(cset)
print(diff)

adiff = nset.symmetric_difference(cset)
print(adiff)

subs = nset.issubset(cset)
print(subs)

supset = nset.issuperset(cset)
print(supset)

'''
1256
x[2]['bar']['z']
'''

x = ['a', 'b', {'foo': 1, 'bar': {'x': 10, 'y': 20, 'z': 30}, 'baz': 3}, 'c', 'd']
print(x)

