data = {
    "name": "Alice",
    "age": 25,
    "city": "Mumbai",
    "profession": "Engineer"
}

key = input("Enter the key you want to find the value of: ")

if key in data:
    print("Value:", data[key])
else:
    print("Key not found!")
