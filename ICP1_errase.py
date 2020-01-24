name = input("Enter something...")
x = input("Enter how many words to erase")
print(name[(len(name) - 1) - int(x)::-1])
