"""
Loops - Execute the same line multiple times
    for loop syntax:
    for <variable> in <some_range>:
        # Code block
        # These lines can be executed more than once
        print("Hello")

    while loop syntax:
    while condition:
        # <code block>
        # These lines can be executed more than once
        print("Hello")
        <UPDATE SOMETHING HERE> # if you don't update then, it will be an infinite loop

    for with list syntax:
    for <variable_name> in <some_list>:
        # Code block
        # These line can be executed more than once
        print("Hello")
"""

# Problem statement: Print user name the number of times the user tells
name = "Anshu"
num = 5
for var1 in range(num):
    print(f"Hello {name}")
"""
Hello Anshu
Hello Anshu
Hello Anshu
Hello Anshu
Hello Anshu
"""

for var1 in range(num):
    print(f"Hello {var1} $ {name}")
"""
Hello 0 $ Anshu
Hello 1 $ Anshu
Hello 2 $ Anshu
Hello 3 $ Anshu
Hello 4 $ Anshu
"""

total_players = input("Enter no. of player: ")
total_players = int(total_players)
for i in range(total_players):
    name = input(f"Enter Player {i+1} name:")
    print(f"Welcome, {name}")
"""
Enter Player 1 name:A
Welcome, A
Enter Player 2 name:B
Welcome, B
Enter Player 3 name:C
Welcome, C
Enter Player 4 name:D
Welcome, D
"""

# for loop is used when you know the start and end of rnage
# while loop is used when you want to run until the output is reached

counting_var = 0
while counting_var < 3:
    print(f"Counting: {counting_var}")
# This will go in an infinite loop and can be stopped with ctrl+C
while counting_var < 3:
    print(f"Counting: {counting_var}")
    counting_var = counting_var + 1

#### for with range ####
bla = [10,20,30,40, 'Anshu', 'Rutu', ["Manav", 'Deepa'], "NixNix"]
for i in range(len(bla)):
    print(f"Element: {bla[i]}") # or print(bla[i])
"""
Element: 10
Element: 20
Element: 30
Element: 40
Element: Anshu
Element: Rutu
Element: ['Manav', 'Deepa']
Element: NixNix
"""

#### for with list ####
bla = [10,20,30,40, 'Anshu', 'Rutu', ["Manav", 'Deepa'], "NixNix"]
for item in bla:
    print(item)
"""
10
20
30
40
Anshu
Rutu
['Manav', 'Deepa']
NixNix
"""

#### for with string ####
bla = "Anshuman"
for i in range(len(bla)):
    print(bla[i])
"""
A
n
s
h
u
m
a
n
"""
# Format 2:
for char in bla:
    print(char)

#### for with break ####
for i in range(10):
    print(i)
"""
0
1
2
3
4
5
6
7
8
9
"""
# What if you wnat to stop printing at 7? then how will you do it?
for i in range(10):
    if i == 7:
        break
    print(i)
    print("hello")
"""
1
hello
2
hello
3
hello
4
hello
5
hello
6
hello
"""

for i in range(10):
    if i < 7:
        print(i)
    print("hello")
"""
0
hello
1
hello
2
hello
3
hello
4
hello
5
hello
6
hello
hello
hello
hello
"""

for i in range(10):
    if i < 7:
        print(i)
        print("hello")
"""
0
hello
1
hello
2
hello
3
hello
4
hello
5
hello
6
hello
"""

for i in range(10):
    print(i)
    break
"""
0 # Only this because the loop was broken after the first i was printed
"""

for i in range(10):
    if i <7:
        break
    print(i)
"""

"""

for i in range(10):
    print(i)
    if i < 7:
        break
"""
0
"""

#### for with continue ####
"""
The break statement killed the whole loop. But what if I only want to kill that iteration and continue the loop
"""
bla = [5, 6, "Manav", 10, "Nix"]
# The propblem statement is to multiply only number by 2
for item in bla:
    print(item*2)
"""
10
12
ManavManav
20
NixNix
"""
# But in this, everything is multiplied by 2
for i in bla:
    if type(i) != int:
        print(i)
        continue
    print(i * 2)
"""
10
12
Manav
20
Nix
"""

# The difference when you use break
for i in bla:
    if type(i) != int:
        print(i)
        break
    print(i * 2)
"""
10
12
Manav
"""

#### zip functions ####

name = ["Anshu", "Rutu", "Nix"]
ages = [30, 27, 25]
# Print as this: Anshu = 30, Rutu = 27, Nix = 25
for i in range(len(name)):
    print(f"{name[i]} = {ages[i]}")
"""
Anshu = 30
Rutu = 27
Nix = 25
"""

list(zip(name, ages))
"""
[('Anshu', 30), ('Rutu', 27), ('Nix', 25)]
"""

for item in zip(name, ages):
    print(item)
"""
('Anshu', 30)
('Rutu', 27)
('Nix', 25)

Now within each index, there are two elements
"""
for item in zip(name, ages):
    print(f"{item[0]} = {item[1]}")
"""
Anshu = 30
Rutu = 27
Nix = 25
"""
"""
Simpler version:
for a, b in zip(names, ages):
    print(f"({a} = {b})")
"""

#### for and enumerate ####
bla = [10, "manav", "30", "rutu"] # only list and string
for idx, val in enumerate(bla):
    print(idx, val)
"""
0 10
1 manav
2 30
3 rutu
"""
list(enumerate(bla))
"""
[(0, 10), (1, 'manav'), (2, '30'), (3, 'rutu')]
"""

for idx, val in enumerate(bla):
    if type(val) != int:
        continue
    bla[idx] = bla[idx] * 2
bla
"""
[20, 'manav', '30', 'rutu']
"""

"""" 
Exercise:

write a program for calculator.

Enter your name: <anshu>
Welcome <anshu> to the calculator world!

What do you want to do?
1. Add
2. Sub
3. Mult
4. Div
5. Exit

Enter your choice (1,2,3,4; add, sub, mul, div): 1/add
Enter first number: 10
Enter second number: 20

Addition of 10 and 20 is 30.
Subtracting 10 from 20 gives 20.
Multiplying 20 with 10 gives 200.
Dividing 20 by 10 gives 2 as quotient and 0 as remainder

What if user entered 0 as denominator:
"Division by zero is not allowed" and return to options

What do you want to do?
1. Add
2. Sub
3. Mult
4. Div
5. Exit

Thank you for using my calculator <anshu>

for - only when you know the limits of the loop
while - when you dont know the number of iterations
"""


name = input("Enter your name: ")
print(f"Welcome {name} to the calculator world!.\nWhat do you want to do?")
choice = input("Enter your choice:\n1. or Addition\n2. or Subtraction\n3. or Multiplication\n4. or Division\n5. or Exit ")

while choice is True:
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))

    if choice == "1." or choice == "Addition":
        print(f"Addition of {num_1} and {num_2} is {num_1 + num_2}")
    elif choice == "2." or choice == "Subtraction":
        print(f"Subtraction of {num_1} and {num_2} is {num_1-num_2}")
    elif choice == "3." or "Multiplication":
        print(f"Multiplication of {num_1} and {num_2} is {num_1*num_2}")
    elif choice == "4." or "Division":
        print(f"Division of {num_1} and {num_2} is {num_1/num_2}")
    elif num == 0:
        print(f"Division by zero is not allowed")
    elif choice == "5." or "Exit":
        print(f"Thank you for using the calculator")
        break



"""
Nested Loops - Loop k andar loop. Everythiong learnt so far in loops is applicable in nested loops. No limit on number of loops in loops.
"""
for i in range(10):
    for j in range(10):
        print(f"{i}{j}")


for i in range(5):
    msg = ""
    for j in range(5):
        msg = f"({i}, {j})\t" 
    print(msg)
    print("\n")
# Not the desired output hence check the next one. In this the output is being replaced every time the loop runs hence only one item is printed in the output.


for i in range(5):
    msg = ""
    for j in range(5):
        msg += f"({i}, {j})\t" 
    print(msg)
    print("\n")


"""
Problem:
rows = 8
cols = 9
We need to print this pattern:
***>
   <***
***>
   <***
***>
"""
rows = int(input("Enter number of row: "))
cols = int(input("Enter number of columns: "))

center = cols // 2

for i in range(rows):
    msg = ""
    for j in range(cols):
        if i % 2 == 0:  # even --> print from left and with >
            if j < center:
                msg = msg + "*"
            elif j == center:
                msg = msg + ">"
            else:
                msg = msg + " "
        else:
            if j < center:
                msg = msg + " "
            elif j == center:
                msg = msg + "<"
            else:
                msg = msg + "*"
    print(msg)


"""
Problem: 
Length of rectanlge from user
Width of rectangle from user

Print the rectangle of length x width

bottomleft = "└"
bottomright = "┘" 
topleft = "┌"
topright = "┐"
horizontal = "─"
vertical = "│"
"""




