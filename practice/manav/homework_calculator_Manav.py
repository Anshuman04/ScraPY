name = input("Enter your name: ")
print(f"Welcome {name} to the calculator world!.\nWhat do you want to do?")

while True:
    choice = input("Enter your choice:\n1. or Addition\n2. or Subtraction\n3. or Multiplication\n4. or Division\n5. or Exit ")
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    
    if choice == "1." or choice == "Addition":
        print(f"Addition of {num_1} and {num_2} is {num_1 + num_2}")
    elif choice == "2." or choice == "Subtraction":
        print(f"Subtraction of {num_1} and {num_2} is {num_1-num_2}")
    elif choice == "3." or choice == "Multiplication":
        print(f"Multiplication of {num_1} and {num_2} is {num_1*num_2}")
    elif choice == "4." or choice == "Division":
        if num_2 == 0:
            print(f"Division by zero is not allowed")
        else:
            print(f"Division of {num_1} and {num_2} is {num_1/num_2}")
    else:
        print(f"Thank you for using the calculator")
        break