contact_info = {
    "Alice": "555-1234",
    "Bob": "555-5678",
}

alice_phone = contact_info["Alice"]
print(alice_phone)

bob_phone = contact_info["Bob"]
print(bob_phone)

contact_info["Alice"] = "123 -456"
print(contact_info)

contact_info["Eva"] = "345-345"
print(contact_info)

del contact_info["Bob"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information = {
    "Alice" : {
        "phone-number" : "555-1234",
        "email" : "alice@gmail.com",
        "birthday" : "01/01/1980"
    },

"Bob": {
    "phone-number": "845-555",
    "email": "bob@gmail.com",
             "birthday": "01/01/1999"
}
}
print(contact_information)
print(contact_information["Bob"])

