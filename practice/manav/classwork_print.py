#### Summary of Print Commands and Variables ####

# This is usage of single quote
print('Hello from Manav 1')

# This is usage of double quote
print("Hello from Manav 2")

#  This is usage of single-double and vice versa
print('"Hello from Manav 3"')
print("'Hello from Manav 4'")

# This is usage of both single-double using single and/or double quote
print("\"Hello from Manav 5'")
print ('\'Hello from Manav 6"')

# To print comments in two lines
print('Hello from \nManav 7')

# This is to use tab feature in print statement
print('Hello from \tManav 8')


"""
Four of the many variable that exit in variables
    Integer (int): -3,-2,-1,0,1,2,3
    Float (float): positive and negative demicals -1.1, 1.1
    String (str): everything in quotes is a string "Manav", 'Manav', "123", '123'
    Boolean (bool): True, False - only types possible, to be used as is and cant be used variable
    NoneType (None): void/means nothing, to be used as is and cant be used variable
"""

# Define variables and check their classes
    # type(<variable>)  replace <variable> with the defined variable
        var1 = 123
        var2 = 123.123
        var3 = 'Manav 123 in single quote'
        var4 = "Manav 123 in double quote"


# Typecasting: the process of converting one variable to another
    # int to str
        int_to_str = str(123)
            print(type(int_to_str))

    # str to int
        str_to_int_1 = int("123")
            print(type(str_to_int_1))
        str_to_int_2 = int("Manav") # Error because characters are not integers
        str_to_int_3 = int("123.1") # Error beacuse decimal are not integers

    # float to int
        float_to_int_1 = int(1.2)
            print(type(float_to_int_1))
    
    # int to float
        int_to_float_1 = float(123)
            print(type(int_to_float_1))

    # float to str
        float_to_str_1 = str("1.2")
            print(type(float_to_str_1))

    # str to float
        str_to_float_1 = float("1.2")
            print(type(str_to_float_1))
        str_to_float_2 = float("Anshuman") # Error because float does not accept characters


# Operations on variables: 
    # Arithmatic: +, -, *, /, //; %; **
        a = 100
        b = 10
        c = 9

        addition = a+b
        subtraction = a-b
        multiplication = a*b
        division = a/b
        division_with_decimal = a/c
        quotient_only = a//c
        remainder_only = a%c
        power = a^b or a**b


    # Logical operations: and, or, not
        """
        Logic for or
            |  |   
         A--|--|--B
        """

        """
        Logic for and
        A--|  |---------|--|--B
        """

        """
        not True
        This will give output as False
        """

# Format printing
    var_5 = 12
    var_6 = "Manav"
    var_7 = 3.14
    var_8 = False

    print(f"Your variable value is {var_5}, whose type is {type(var_5)}")
    print(f"Your variable vaule is {var_6}, whose type is {type(var_6)}")
    print(f"Your variable vaule is {var_7}, whose type is {type(var_7)}")
    print(f"Your variable vaule is {var_8}, whose type is {type(var_8)}")
    print(f"Printing after calculation: {var_5+var_7}")

    # User input
        name = input("Enter your name: ")
        print(f"Hello {name}.")

        # The output is always a str type. If a number is expected as input, then ensure to use typecasting to convert str to int
            age = input("What is your age: ")
            age
            # NOTE: age+5 will give error as the type is string for age entered.
            
            # Alternative 1
                age = int(input("What is your age: "))
                age + 5

            # Alternative 2
            age = input("What is your age: ")
            age = int(age)
            age = 5

    # Assignment operator
        var_9 = 10
        var_9 = var_9 + 20
    
    # Comparators always give output as either True or False
        # ==
            2 == 2 # True
            2 == 3 # False

        # != where the exclamation means not
            2 != 2 # False
            2 != 3 # True

        # Standard mathematical operations which will also give outputs as True or False
            #<
            # <=
            # >
            # >=










