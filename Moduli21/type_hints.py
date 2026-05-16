def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()   #title e ban shkronjen e par tmadhe
    return full_name

print(get_full_name("John", "Doe"))