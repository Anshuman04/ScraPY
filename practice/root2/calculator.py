name = input("Enter your name: ")
print(f"Welcome {name} to the calculator world!")
while True:
    print(f"What do you want to do?\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Exit")
    option = input("Enter your option: ")
    print(f"You entered {option}")
    if option == "Exit" or option == "5" or option == "exit":
        break
    var1 = int(input("Enter your first number: "))
    var2 = int(input("Enter your second number: "))
    if option == "Addition" or option == "1" or option == "add" or option == "Add" or option == "addition":
        print(f"Addition of {var1} and {var2} is {var1 + var2}")
    elif option == "Subtraction" or option == "2" or option == "sub" or option == "Sub" or option == "subtraction":
        print(f"Subtraction of {var1} from {var2} is {var1 - var2}")
    elif option == "Multiplication" or option == "3" or option == "mul" or option == "Mul" or option == "multiplication":
        print(f"Multiplication of {var1} with {var2} is {var1 * var2}")
    elif option == "Division" or option == "4" or option == "div" or option == "Div" or option == "division":
        if var2 == 0:
            print ("Division by zero is not allowed")
            continue
        else:
            print(f"Dividing {var1} by {var2} gives {var1 // var2} as quotient and {var1 % var2} as remainder")