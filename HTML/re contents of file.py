file = open("Codingal.txt","r")
Counter = 0
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        Counter += 1

print("this is the number of line in the file")
print(Counter)