phonebook = {}

def add_contact(name, number):
    if name in phonebook:
        print(f"contact '{name}' alredy exists Updating the number.")
    phonebook [name]= number
    print(f"contact '{name}'added/updated successfuly.")

def search_contact(name):
    if name in phonebook:
        print(f"{name}:{phonebook[name]}")

    else:
        print(f"contact'{name}'not found.")

def delete_contacts(name):
    if name in phonebook:
        del phonebook [name]
        print(f"Contacts'[name]' deleded.")
    else:
        print(f"Contact '[name]'not found.")

def display_contact ():
    if phonebook:
        print("\n 📖 Phonebook Contacts :")
        for name, number in phonebook.items():
            print(f"{name}:{number}")

        else:
            print("Phonebook is enpty")