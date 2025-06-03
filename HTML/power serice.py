x = int(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

print("Power series:")

for i in range(n):
    term = x ** i
    print(term)