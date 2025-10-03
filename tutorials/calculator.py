


# 1. Take name from user
# 2. Greet User
    # 3. Print menu
    # 4. Take choice input from user
    # 5. Take 2 numbers
    # 6. a+b, a-b, a*b, a/b

def take_two_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1, num2

def take_multiple_numbers(nums):
    result = []
    for num in nums:
        result.append(int(input(f"Enter number {num}: ")))
    return result

def print_menu_and_get_choice():
    print("1. Addition\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def exit_if_required(choice):
    if choice == 5:
        exit()

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        print("NOT ALLOWED")
    return num1 / num2

def select_calculate_function(choice):
    # return [addition, subtraction, multiplication, division][choice - 1]
    if choice == 1:
        return addition
    elif choice == 2:
        return subtraction
    elif choice == 3:
        return multiplication
    elif choice == 4:
        return division


name = input("Enter your name: ")
print(f"Hello {name}")

while True:
    choice = print_menu_and_get_choice()
    exit_if_required(choice)
    num1, num2 = take_two_numbers()
    calculate_function = select_calculate_function(choice)
    result = calculate_function(num1, num2)
    print(f"RESULT: {result}")