a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}


def update_dictionary(a_dictionary, key, value):
    for keys in a_dictionary:
        if keys == key:
            a_dictionary[keys] = value
        else:
            a_dictionary[key] = value
        return a_dictionary
new_dict = update_dictionary(a_dictionary, 'language', "Python")
new_dict = update_dictionary(a_dictionary, 8, "string")

print(new_dict)