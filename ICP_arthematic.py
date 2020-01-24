Uin = input("enter any two numbers")
L = Uin.split(",")
x = L[0]
y = L[1]
Operation = input("Enter which operation to perform")
if Operation == "sum":
    print(int(x)+int(y))
elif Operation == "subtraction":
    print(int(x) - int(y))
elif Operation == "Multiply":
    print(int(x) * int(y))
else : print(int(x) / int(y))

