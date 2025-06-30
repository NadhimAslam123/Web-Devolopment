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

def phonebook_menu ():
    while True:
        print("\n======Phonebook Menu======")
        print("1. Add/Update Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Exit")

        Choice = input ("Enter your Choice (1-5):")

        if Choice == '1':
         name = input ("Enter name:")
         number = input ("Enter number:")
         add_contact(name,number) 

        elif Choice == '2':
            name = input("Enter name to search:")
            search_contact(name)
        elif Choice == '3':
            name = input ("Enter name to delete:")
            delete_contacts(name)
        elif Choice == '4':
            display_contact()
        elif Choice == '5':
            print("Exiting phonebook . Godbye!")

phonebook_menu()