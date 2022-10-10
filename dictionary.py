names = {5: "seyi", 6: "ade", 7: "Segun"}
if 3 in names:
    print(names[3])

names.pop(6)
names[6] = "Tade"
print(names)

names[4] = "dell"
names[5] = "dkola"

names[2] = "femi"
names['bae'] = 'song'
print(names[])
print(len(names))
nnames = list(names)
cnames = list([x for x in names])
for keys in names:
    print(keys, names.get(keys), sep=': ')
    #print(keys, names[keys], sep=': ')

# making a dictionary
'''
dic methods clear, getitems, keys, pop,popitems, values,


names.clear()
print(names)

names[1] = "Seyi"
names[2] = "Peter"
names.items()
#print(names)
names.items()
names.keys()
names.get()
'''