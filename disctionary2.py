customer = {
    "name": "John Saint",
    "age": 30,
    "is_verified": True
}
#print(customer.get("birthdate", "1st October"))

phone = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four"
}
output = ""
for key in phone:
    output += phone.get(key, "!") + " "
    #print("{}".format(phone.get(key)), sep='')
#print(output)


'''
Dictionary methods
'''
def message_emoji(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😕"
    }
    newoutput = ""
    for word in words:
        newoutput += emojis.get(word, word) + " "
    return newoutput


greetings = input(">")
print(message_emoji(greetings))