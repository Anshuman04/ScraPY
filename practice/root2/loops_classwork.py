TYPES OF LOOPS: 
1) FOR
2) WHILE

WHAT IS FOR LOOPS? 
"""FOR: It is a function used to execute the same line multiple times when you know the start and end point.
SYNTAX FOR LOOPS:
for <your variable> in <a range of your choice>:
    # Code Block
    # These lines can be executed more than once
    print("Hello")
"""
Eg: 
name = "Anshu"
num = 5
print(f"Hello {name}") #gives output: Hello Anshu

"""WHAT IS RANGE? It basically internally processes the below thing:
range(<start_counting_here_inclusive>, <stop_counting_here_exclusive>, <step>)
"""
Eg:
for var1 in range(num):
    print(f"Hello {var1} $ {name}")

#output: 
Hello 0 $ Anshu
Hello 1 $ Anshu
Hello 2 $ Anshu
Hello 3 $ Anshu
Hello 4 $ Anshu

"""NOTE: var1 here is storing the current values of the determined range"""

To actually print Anshu 5 times: 
for var1 in range(num):
    print(f"Hello {name}")

#output: 
Hello Anshu
Hello Anshu
Hello Anshu
Hello Anshu
Hello Anshu

To be able to take input, print, take input, print again and again. Basically, can put any number of lines that you want to loop over.
total_players = input("Enter no. of players: ")
total_players = int(total_players)
for i in range(total_players):
    name = input(f"Enter Player {i+1} name:")
    print(f"Welcome, {name}")

WHAT IS WHILE LOOP? 
"""WHILE: Keeps printing till the condition is true
SYNTAX FOR WHILE: 
while condition:
    # Code Block
    # These lines can be executed more than once
    print("Hello")
    <UPDATE SOMETHING HERE> #vvvvvvvvvv important otherwise it will be an infinite loop or a loop that never executes 
"""

Eg:
counting_var = 0
while counting_var < 3:
    print(f"Counting: {counting_var}")
    counting_var = counting_var + 1

#Output: 
Counting: 0
Counting: 1
Counting: 2 

FOR LOOPS WITH LISTS: 

bla = [10, 20, 30, 40, "Anshu", "Rutu", ["Manav", "Deepa"], "Nix"*2]
for i in range(len(bla)):
    print(f"Element: {bla[i]}")

#Output: 
Element: 10
Element: 20
Element: 30
Element: 40
Element: "Anshu"
Element: "Rutu"
Element: ['Manav', 'Deepa']
Element: NixNix

"""SYNTAX FOR LISTS IN FOR LOOP:
for <variable name> in <some_list>:
    # Code Block
    # These lines can be executed more then once
    print("Hello")""" 

Eg: 
bla = [10, 20, 30, 40, "Anshu", "Rutu", ["Manav", "Deepa"], "Nix"*2]
for i in bla:
    print(f"Element: {i}")

#Output: 
Element: 10
Element: 20
Element: 30
Element: 40
Element: "Anshu"
Element: "Rutu"
Element: ['Manav', 'Deepa']
Element: NixNix

FOR LOOPS WITH STRINGS: 

name = "Anshuman"
for i in name: 
    print(i)

#Output: 
A 
n 
s 
h 
u 
m 
a 
n 

FOR LOOPS WITH BREAK: 

for i in range(10):
    print(i)

#Output: 
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
10

for i in range(10):
    if i == 7:
        break
        print(i)

#Output:
0
1
2
3
4
5
6

for i in range(10):
    if i == 7:
        break
        print(i)
        print("Hello")

#Output: 
0
Hello
1
Hello
2
Hello
3
Hello
4
Hello
6
Hello

for i in range(10):
    if i < 7:
        break
    print(i)

#Output: 
"""it won't print anything cause the first condition got satisfied 
since 0 < 7 and the code broke due to the break function"""

for i in range(10):
    print(i)
    if i < 7:
        break

#Output: 
0

FOR WITH CONTINUE: 

blah = [5, 6, "Manav", 10, "Nix"]
for i in blah:
    print(i*2)

#Output:
10
12
ManavManav
20
NixNix
 
for i in blah:
    if type(i) != int:
        print(i)
        continue
        print(i * 2)

#Output: 
10
12
Manav
20
Nix

ZIP FUNCTION IN FOR LOOPS:

name = ["Anshu", "Rutu", "Nix"]
age = [30, 27, 25]

for i in range(len(name)):
    print(f"{name[i]}={age[i]}")

#Output: 
Anshu=30
Rutu=27
Nix=25

"""That was a very complicated line of code, we can instead use zip function"""

list(zip(name, age))

#Output: 
[('Anshu', 30), ('Rutu', 27), ('Nix', 25)]

for item in zip(name, age):
    print(f"{item[0]}={item[1]}")

#Output: 
Anshu=30
Rutu=27
Nix=25

for item in zip(name, age): print(item)

#Output: 
('Anshu', 30)
('Rutu', 27)
('Nix', 25)

"""That was a very complicated line of code, we can instead do this:""""

for a, b in zip(name, age):
    print(f"{a}={b}")

#Output:
Anshu=30
Rutu=27
Nix=25

ENUMERATE FUNCTION IN FOR LOOPS: 
bla = [10, 'manav', 30, 'rutu']
for idx, val in enumerate(bla):
    if type(val) != int:
        continue
    bla[idx] = bla[idx] * 2
    print(bla)

#Output:
[20, 'manav', 60, 'rutu']


EXERCISE: 

write a program for calculator.

Enter your name: <anshu>
Welcome <anshu> to the calculator world!

What do you want to do?
1. Add
2. Sub
3. Mul
4. Div
5. Exit

Enter your choice (1,2,3,4,5; add, sub, mul, div, exit): 1/add
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

NESTED LOOP: loops inside loops

for i in range(10):
    for j in range(10):
        print(f"(i)(j)") 

#Output:
"""it'll print 00, 01, 02, 03.... to 99 all numbers"""

PRINTING LOCATIONS OF CELLS IN EXCEL SHEET:

for i in range(5):
    msg = ""
    for j in range(5):
        msg = msg + f"({i}, {j})\t"
    print(msg)
    print("\n\n")

PROBLEM STATEMENT: 
rows = 8
column = 9 
PRINT: 
***>
   <***
***>
   <***
***>
   <***

ANSWER: Only for odd number of columns 

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
center = cols // 2

for i in range(rows):
    msg = ""
    for j in range(cols):
        if i % 2 == 0:
            if j < center:
                msg = msg + "*"
            elif j == center:
                msg = msg + ">"
            else:
                msg = msg + " "
        else:
            if j > center:
                msg = msg + "*" 
            elif j == center:
                msg = msg + "<"
            else:
                msg = msg + " "     
    print(msg)

PRACTICE PROBLEM: 
TAKE: 
length of recantangle from user
width of recantangle from user

USE THE FOLLOWING CHARACTERS: 
bottomleft = "└"
bottomright = "┘" 
topleft = "┌" 
topright = "┐" 
horizontal = "─" 
vertical = "│"

PRINT: 
print the rectangle share of the given length and width 

