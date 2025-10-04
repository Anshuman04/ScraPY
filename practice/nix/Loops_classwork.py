# Loop ka kaam hota hai ki woh software flow ko peeche bhi lekar jaaye. Its executing the same line multiple times. so it needs to have a breaking point as well ki kab tak iss loop mein rehna hai

"""
SYNTAX:
1. For loop: yahan se yahan tak chalao is the essence of this loop

for <variable_name> in <some_range>:
    # code block
    # these lines can be executed more than twice
    print("Hello")
"""

# range(<start_counting_here_inclusive>, <Stop_counting_here_exclusive>, <step>)    by default it starts from 0 and step is 1
# range(5) --->   this will internally count from 0 to 5

"""
EXAMPLE CODE:

name = "Nix"
num = 5
for var1 in range(num):
    print(f"Hello {var1} $ {name}")

var1 stores the current count in the range. If the range was from (10,16) the var1 values will be 10, 11, 12, 13, 14, 15
    
This will print: 
Hello 0 $ Nix
Hello 1 $ Nix
Hello 2 $ Nix
... and so on for 5 times

ANOTHER EXAMPLE:
total_players = input("enter no. of players: ")
---> Enter no. of players: 4
total_players = int(total_players)

for i in range(total_players):
    name = input(f"Enter player {i + 1} name: ") 
    print(f"Welcome, {name}")

---> Enter player 1 name: Nix
    Welcome Nix
    ENter player 2 name: Rutu
    Welcome Rutu
    .... and so on

Here i is storing the range values i.e from 0 to 3, and while printing it takes i+1 so its rpinting from 1 to 4
"""
"""
2. WHILE LOOP: jab tak yeh condition true hai tab tak chalao

while <condition>:                    --> Condition can be evaluated as true and false
    #code_block
    #these line can be executed more than once
    print("Hello")
    <Update_something_here>
"""

counting_var = 0
while counting_var < 10:
    print(f"Counting: {counting_var}")
    counting_var = counting_var + 1                 # here we are updating the counting_var value warna woh infinite loop hai.

are_players_joining = True
joined_players = []
while are_players_joining:
    name = input("Enter player name: ")
    joined_players.append(name)
    if name == "done":
        are_players_joining = False

"""
bla = [10, 20, 30, 40, "Anshu", "Rutu", ["Manav", "Deepa"], "Nix"*2]
for i in range(len(bla)):
    print(f"Element: {bla[i]}")
"""
"""
FOR WITH LISTS:
for <variable_name> in <some_list>:
    #code_block
    #these line can be executed more than once
    print("Hello")

bla = [10, 20, 30, 40, "Anshu", "Rutu", ["Manav", "Deepa"], "Nix"*2]
for item in bla:
    print(item)

    yahan pe item pe har element print ho raha hai. its similar to when we do list(range(4))
    yeh hume deta hai [0, 1, 2, 3] and technically woh har element ko print kar raha hai
    ussi tarah print(item) pe woh har element print karega uska index nahi
"""
"""
FOR WITH STRINGS:
abc = "Nikitha"                     This is like saying 
for char in abc:                    for i in range(len(abc))    -----> This will take [0,7] in a list which is [0, 1, 2, 3, 4, 5, 6]
    print(char)                     print(abc[i])               -----> This will give each item in that index i

This will give
N
i
k
i
t
h
a
"""
"""
FOR WITH BREAK: You can break the loop anytime you want. 
for i in range(10):
    if i == 7:
        break
    print(i)
    print("Hello")

Yahan pe loop band ho jaayega jab i ki value 7 ho jaayegi. but agar maine likha hota if i < 7; and if ke andar print statements likti, toh same output aata but loop phir bhi 
chal raha hai. so its like if you want to find an element in a range of say 10^9 elements then you can break once you find it instead of making the machine go through the entire range.
break jahan daaloge toh wahan woh loop se bahar aajayega.
"""
"""
FOR WITH CONTINUE: agar aapko koyi iteration band karna hai toh yeh use kar sakte ho

bla = [ 5, 6, "Manav", 10, "Nix"]
for item in bla:
    print(item*2)     Yeh har element ko *2 kar dega. agar hume sirf numbers ko multiply karna hai toh do the following

for item in bla:
    if type(item) != int:
        print(item)                agar item integer nahi hai toh seedha seedha print karega
        continue                    aur continue karega to the next element with the condition by killing the current iteration. agar break daal dete toh poora loop hi kill ho jaata Manav pe
    print(item * 2)

---> 10
    12
    Manav
    20
    Nix

bla = [ 5, 6, "Manav", 10, "Nix"]
result = []
for item in bla:
    if type(item) != int:
        result.append(item)
        continue
    result.append(item*2)

---> [10, 12, "Manav", 20, "Nix"]      in this case a new list will be printed

bla = [ 5, 6, "Manav", 10, "Nix"]
for i in range(len(bla)):
    if type(bla[i]) != int:
        continue
    bla[i] = bla[i] * 2

---> [10, 12, "Manav", 20, "Nix"]     iss case mein bla update ho raha hai.
"""

name = ["anshu", "rutu", "nix"]
age = [30, 27, 25]
for i in  range(len(name)):
    print(f"{name[i]} = {age[i]}")

"""
ZIP: Instead of doing the above labor we can use zip.

list(zip(name,age))   -----> this will return a new list [('anshu',30), ('rutu', 27), ('nix', 25)]
in this list the first element is ('anshu',30) ....this is type a data str called tuple(not required for us)

for item in zip(name, age):
    print(f"{item[0]} = {item[1]}")    

zip(name,age) ka pehla item is ('anshu',30). 
aur iska item[0] = anshu  and item[1] = 30

when we go to the next iteration, which is the next item of zip(name,age) and that is ('rutu', 27)
aur iska item[0] = rutu and item[1] = 27

hum seedha seedha list(zip(name,age)) ko print karenge toh woh  [('anshu',30), ('rutu', 27), ('nix', 25)] yeh print karega. 
but we want anshu = 30 so we do the second option. 

one more way to do this is
for a,b in zip(name,age):
    print(f"{a} = {b}")

"""
"""
ENUMERATE: yeh basically har element ka actual value and the index of that element:

bla = [10, 20, 'manav', nix']
for idx,val in enumerate(bla):
    print(idx,val)

yeh print karega:
0 10
1 20
2 manav
3 nix

for idx, val in enumerate(bla):
    if type(val) != int:
        continue
    bla[idx] = bla[idx] * 2       

iss code mein goal hai ki sirf integer elements ko 2 se multiply karna hai.
type(val) is first checking is its int or not
and then using bla[idx] * 2 we are multiplying the particular value with 2. you can also type val * 2
but we have to assign it to bla[idx] so that bla gets updated. 



"""
"""
Write a prgram for calculator:

Take user input for name
then display, welcome anshu to the calculator world
then ask used "what do you want to do?
1. add
2. sub
3. mul
4. div
5. exit
enter your choice: "   (here you can take the numbers of the option choice or the word itself)

after getting operator choice, ask the user for numbers
"enter first number"
"enter second number"

"addition nd <second no> is <result>" or "subtracting <firstno> from <secondno> gives" or "Multiplying <first no> with <second no> gives" or
"dividing <first no> by <secondno> gives <quo> as quotient and <rem> as remainder. 

if second number is 0 then print "division by 0 is not allowed" and again ask ""what do you want to do?
1. add
2. sub
3. mul
4. div
5. exit
enter your choice: "

if the user choses 5(exit) then it should say "thank you for using my calculator"
once you give an answer for the operation then after printing result ask again,

then again ask "what do you want to do?
1. add
2. sub
3. mul
4. div
5. exit
enter your choice: "

code should run till the user doesn't selects 5(exit)
"""
"""
NESTED LOOPS: Loop ke andar loop. The secondary loop will be executed firstloop rnage * second loop range times
for i in range(10):
    for j in range(10):
        print (f"{i}{j})


for i in range(5):
    msg = ""
    for j in range(5):
        msg = msg + f"({i}, {j})\t"
    print(msg)
    print("\n\n")

""" 
row = int(input("Enter number of rows: "))
col = int(input("Enter odd number of columns: "))

center = col // 2
for i in range(row):
    msg = ""
    for j in range(col):
        if i % 2 == 0:
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

            

        