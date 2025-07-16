def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return ("Error can not divide by zero")
    return a / b
def calculator():
    print("Welcome to basic calculator")
    while True:
        print("\nChoose an operation")
        print("1. Add")
        print("2. substract")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        Choice = input("Enter choice (1-5):")
        if Choice == ("5"):
            print("GoodBye")
            break

        if Choice not in [1,2,3,4]:
          print("Invalid choice. Pleace try again")
          continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if Choice == '1':
            result = add(num1, num2)
        elif Choice == '2':
            result = subtract(num1, num2)
        elif Choice == '3':
            result = multiplication(num1, num2)
        elif Choice == '4':
            result = divide(num1, num2)
        else:
            print("Invalid choice.")
            continue

        print("Result:", result)

calculator()