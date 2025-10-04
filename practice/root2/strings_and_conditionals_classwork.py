#CODE SYNTAX: 
if <Condition>:
    <if block>
else:
    <else block>

#Eg: 
if True:
    print("I am if block")
else:
    print("I am else block")

#Output: I am if block

if False:
    print("I am if block")
else:
    print("I am else block")

#Output: I am else block

#Can put any comparator in the <Condition> section.

MEMBER OPERATORS: 
#is: ==
#in: search function

IMPORTANT TOOLS FOR SELF-LEARNING:
var1 = 10
var2 = Anshuman

print(dir(var2)) #this is the syntax
dir([]) #if I want to know about a list
dir("") #if I want to know about a string
dir(int) #if I want to know about a integer variable 

print(var2.count.__doc__)

--BEGINNING OF NIX CLASS NOTES:

"""
if<condition>:
    <if-block>
    can be multiline also
else:
    <else block>

    
--> You can write just a if statement only 
if <condition>:
    if block

"""
"""
IF-ELIF-ELSE SYNTAX:

if <condition>:
    <if block>
elif <condition>:
    <elif block>
else:
    <else block>
"""
# the conditions can be anything that returns True or False. this means that the if statement just cares about True or False
# so you can also write directly:

"""
if True:               This will print yes
    print("yes")
else:
    print("no")  

if False:               This will print no
    print("Yes")
else:      
    print("No")
"""
# you can use any comparator in the condition.
"""
You can combine two conditions using logical oprators. For eg:


baarish = True
chatha = None
go_out = True

"""
baarish = False   #you can change this conditions and accordingly output will change
go_out = False

if baarish and go_out:
    print("get your umbrella")
elif baarish and not go_out:
    print("Chup chap baith ghar mein. Chai pee")
elif not baarish and go_out:
    print("Bindaas bahar jaa")
else:
    print("WTF?? khud soch le")

# cond1 and (cond2 or cond3)   in case of 3 conditions, and 1 being required and optional between 2 and 3 this syntac can be used

"""
--> MEMBER OPERATORS: is and in

1. is: hai kya?  is operator is kind of like ==
    "Anshu" is "Anshu"


2. in: ismein    
    "Anshu" in "Anshuman"  This will return true
    "Rutu" in Anshuman" This will return False . Its like Control+F for strings

if "Anshu" in "Anshuman":           This will give true so if block will be executed
    print("Search found")
else:
    print("search not found")

"""

v1 = 0
v2 = 1
if v2:                         # here since v1 = 0 it wont execute anything when you write 'if v1'
    print("Success")            # if v2 will be excecuted for any number including decimals and negative. Because 0 is equivalent to blank. blank will be taken as false

# with if <something> we are basically checking if it has something. so if the data structure is blank it wont execute the if statement.
# every data str has a blank version. For int, its 0; float its 0.0; str its empty str; bool its False.


num =int(input("enter numerator: "))
den = int(input("enter denominator: "))

if not den:                        # not den is same as writing den == 0
    print("denominator can not be 0")
    exit()

print(f"Quotient is {num//den}")

"""
--> EXTRA INFO TO GET INFO:
v1 = 10
v2 ="Nix"
print(dir(v2))    -----> This will tell you all the functions that you can use for this variable. Ignore the functions that start with an underscore (thats for developers)

--> DUNDER DOC (double underscore doc)
print(v2.)   ---> read this as 'string ka'
print(v2.count.__doc__)  ----> yeh batayega ki string ka count kya karta hai?

"""

"""
--> STRINGS:

Each character of a string wil have an index number that starts with 0

name = "Nikitha"
name[0] --> This will give N
name[1] --> This will give i

1. Slicing:
<variable_name>[<start_index>:<end_index>]  The end-index is not included. so if you want Niki, the command is
name[0:4]

If you want alternate characters, you can also jump,
<variable_name>[<start_index>:<end_index>:<step_size>]     by default step size is 1. so if you dont mention anything it will print every character. 
name[0:7:2]   This will give me every 2nd character

other alternative to this is
name[::2]  this is taking by default start to end
name[2:]  this takes kitha  from 2nd till end

--> Negative slicing:
The last digit of the string has the index -1. and it begins from back -1, -2 , -3
so in case of niki, the indexing is -4, -3, -2, -1

if i want to print form right to left, i.e., reverse
name[::-1]  this will print the entire string in reverse

"""

END OF NIX KA NOTES FOR THE CLASS--

LIST: It is a collection of data structure. This is also a type of variable.

var1 = [] #to declare a blank list, this is the syntax
type(var1) #checking what is the type of variable that var1 is falling into 
#Output: <Class 'list'> 

var2 = [10, 20, 30, 40, 50] #Eg: this is an example of list

#HOW DO I STUDY THIS LIST? SEE BELOW: 

type(var2[0])
<class'int'>

We can basically do all the search functions we perform on string on a list as well, as shown below, here, everything in # is an Output:
var2[0] #10
var2[1] #20
var2[2] #30
var2[:4] #[10, 20, 30, 40]
var2[2:] #[30, 40, 50]
var2[::-1] #[50, 40, 30, 20, 10]
var2[2:len(var2)-1] #[30, 40]

HOW DO I CHECK THE LENGTH OF MY STRING OR LIST? Function: len(); See example below of how it works: 
name = Anshuman Gaharwar
var2 = [10, 20, 30, 40, 50]
len(name) #17
len(var2) #5

HOW DO I REPLACE OR EDIT A LIST VARIABLE?
var2 = [10, 20, 30, 40, 50] 
Here, var2[2] #30
But if I execute below code: 
var2[2] = 35
Then var2 changes to: 
var2 = [10, 20, 35, 40, 50]

HOW DO I ADD SOMETHING TO MY LIST VARIABLE? 
if I execute: 
var2.append(90)
var2[10, 20, 35, 40, 50, 90]

PYTHON CAN COOK KHICHDI, PLEASE SEE BELOW HOW: 

var2.append("Anshuman")
var2.append(3.14)
var2.append(True)
var2.append(None)
other_list = [1, 2, 3]
var2.append(other_list)

Below see how var2 will look now: 
var2 = [10, 20, 35, 40, 50, 90, 'Anshuman', 3.14, True, None, [1, 2, 3]]

HOW DO I OVERWRITE A VARIABLE? Assign var2 a new list: 
var2 = [10, 20, 30]
other_list = [1, 2, 3]

PROBLEM STATEMENT: 
var2.append(other_list)
var2 = [10, 20, 30, [1, 2, 3]]
len(var2) #4
#Here, the other_list components that I added are being counted as a single variable instead of individual variables, what do I do? 

EXTEND: 
var2.extend(other_list)
var2 = [10, 20, 30, 1, 2, 3]
len(var2) #6
#Now, the components of other_list just got added to the original var2 list individually

HOW DO I USE THE INSERT FUNCTION?
print([].insert.__doc__) 
"""
Insert object before index. 
""" #note: You have to write the index of where you want to add the component into the list
var2.insert(2, 25)
var2 will now become: 
var2 = [10, 20, 25, 30, 1, 2, 3]

HOW DO I USE THE REMOVE FUNCTION? 
print(var2.remove.__doc__)
"""
Remove first occurrence of value. 
""" #note: It can only be used to remove 1 component at once
var2.remove(25)
var2 will now become: 
var2 = [10, 20, 30, 1, 2, 3]

HOW DO I USE POP FUNCTION? #Pop function is used to extract component from your current list to another place so that you do not lose the data (which happens in case of the remove function)
queue = ["Anshuman", "Manav", "Rutu", "Nix"]
processing = []

PROBLEM STATEMENT: How do I remove Anshuman from queue without losing Anshuman? 
name = queue.pop(0)
this will make name give you the output #Anshuman """this basically means that Anshuman has been removed from the list"""
processing.append(name)
['Anshuman']
now, queue will become: 
queue = ["Manav", "Rutu", "Nix"]

#Can also combine the two codes to increase efficiency: 
processing.append(queue.pop(0)) 
This will result in: 
queue = ["Manav", "Rutu", "Nix"]
processing = ['Anshuman']

HOW DO I USE THE COUNT FUNCTION? Question: what are the number of zeros in the given list? 
var = [1, 2, 3, 0, 5, 4, 0, 9, 8, 0]
var.count(0) #3

#can also be used in strings, not just in list. 

"anshuman".count("a") #output: 2 (since there are 2 "a")

HOW DO I USE THE INDEX FUNCTION? #gives you the index of the first occurence only in a list
print([].index.__doc__)
"""Return first index of value"""
var2 = [10, 20, 30, 1, 2, 3]
var.index(30) #2
var[2] #30

#can also be used in strings, not just in list. 

"anshuman".index("a") #output: 0 (since position of first occurence of a is 0)

HOW DO I USE THE REVERSE FUNCTION? He taught us two ways: 

1st way (here, we will preserve the original list and create a new reverse list):

rev_var2 = var2[::-1] 
now, if we run rev_var2 we will get output # [3, 2, 1, 30, 20, 10]
but var2 will still give output # [10, 20, 30, 1, 2, 3]

2nd way (here, we will directly reverse the original list)
var2.reverse()
now, if we run var2 we will get output # [3, 2, 1, 30, 20, 10] 

HOW DO I USE THE SORT FUNCTION? #works in ascending order by default 
var2.sort() will give output # [1, 2, 3, 10, 20, 30]

BUT THEN, HOW DO I USE SORT FOR DESCENDING ORDER? 
var2.sort(reverse=True) will give # [30, 20, 10, 3, 2, 1]

HOW DO I DELETE CONSECUTIVE COMPONENTS THROUGH SLICING?
hihi = [75, 33, 8, 20, 1, 0]
hihi[0:2] will give output # [75, 33]
hihi[4:] will give output # [1, 0]
now, 
hihi[0:2] + hihi[4:] will give output # [75, 33, 1, 0]

q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x, y =  q[::2], q[1::2]
x will then give output # [1, 3, 5, 7, 9]
y will then give output # [2, 4, 6, 8, 10]

---

EXERCISE: 

var = [10, 20, 30, 40, 50, 20, 10, 40, 50, 60, 10]
num = int(input("Enter a number: "))

Delete second occurance of that number and print the remaining list. 

ANSWER:

left = var[:var.index(num)+1]
right = var[var.index(num)+1:]
right.pop(right.index(num))
print(var)
print(left + right)

---

TYPES OF STRING FUNCTIONS: 

IS UPPER FUNCTION: checks if everything is in lower case

"Anshuman".isupper() #Output: False (since every letter is NOT in upper case)
"ANSHUMAN".isupper() #Output: True (since all the letters is in upper case)
"aNshu"[1].isupper() #Output: True (since N, which is in the 1st index is in upper case)
"".isupper() #False 

IS LOWER FUNCTION: checks if everything is in lower case

#it works exactly the same as the #isupper function (syntax included). 

LOWER FUNCTION: converts the entire string to lower case

"ANSHU".lower() #Output: 'anshu'
"aNshU".lower() #Output: 'anshu'
"anshu".lower() #Output: 'anshu'

UPPER FUNCTION: has the same syntax and working as the lower function

#lower and upper function are not conditionals (they don't give the output True or False) 
#but you can use it inside a full condition, where there is another conditional operator (for example: <; >; ==; !=)

IS TITLE FUNCTION: it checks if the first letter is capital and everything else in lower case 

"Anshu".istitle() #Output: True
"anshU".istitle() #Output: False
"Anshuman Gaharwar".istitle() #Output: True 

IS DIGIT FUNCTION: it checks if all the characters in a string are digits

"24".isdigit() #Output: True
"24.2".isdigit() #Output: False (since decimal point is not a digit)

USE CASE OF THESE FUNCTIONS: Eg: 

while True: 
    inp = input("Enter a num: ")
    if not inp.isdigit():
        print("Please enter a number")
        continue 
    num = int(inp)
    break 

IS ALPHA NUMERIC FUNCTION: it checks if the string has alphabet OR number

"anshu".isalnum() #Output: True
"anShu".isalnum() #Output: True
"anShu07".isalnum() #Output: True
"anshu07$".isalnum() #Output: False
"anShu07_9".isalnum() #Output: False 

IS ALPHA FUNCTION: it checks if the string has only alphabets

"anshU".isalpha() #Output: True
"aNshU07".isalpha() #Output: False

SPLIT FUNCTION: it splits a string and gives the output in the form of a list

bla = "Anshuman is teaching python"
bla.split() #Output: ['Anshuman', 'is', 'teaching', 'python']

now lets check if the above output is actually falling in the "list" category:-
result = bla.split()
type(result) #Output: <class'list'>

bla.split().pop(0) #Output: 'Anshuman'
bla.split().pop(0).upper() #Output: 'ANSHUMAN'

blah = "Anshuman is teachingpython"
blah.split() #Output: ['Anshuman, 'is', 'teachingpython'] 
"""NOTE: the above output is confirming that space is the separator that is crucial for what elements
come in the list"""

ball = "Anshuman_Gaharwar_22987_30"
ball.split("_") #Output: ['Anshuman', 'Gaharwar', '22987', '30']
"""NOTE: I can tell the split function where to separate but the defined separator gets eliminated never becomes part of the list"""

"anshuman loves chocolate and icecream".split("an")
#Output: ['', 'shum', ' loves chocolate ', 'd icecream'] 
"""NOTE: see in the above output how "an" is removed everywhere"""

"anshuman".split("anshuman")
#Output: ['', '']

USE CASE EXAMPLE OF THIS CONCEPT: 

bla = ["Anshuman_Gaharwar_22987_30", "Rutu_Mishra_1600401_27"]
for person in bla:
    first_name, second_name, employee_id, age = person.split("_")
    print("="*40)
    print(f"First name: {first_name}")
    print(f"Second name: {second_name}")
    print(f"Employee ID: {employee_id}")
    print(f"Age: {age}")

#Output: 
========================================
First name: Anshuman
Second name: Gaharwar
Employee ID: 22987
Age: 30
========================================
First name: Rutu
Second name: Mishra
Employee ID: 1600401
Age: 27

ANOTHER USE CASE: 

novel = "This is first line.\nThis is second line"
sentences = novel.split("\n")
#Output: ['This is first line.', 'This is second line']

SPLITLINES FUNCTION: 

novel = "This is first line.\nThis is second line"
novel.splitlines()
#Output: ['This is first line.', 'This is second line']

STRIP FUNCTION: it removes the space from both sides of the string, where
space is a default delimitor: 

 " anshu ".strip()
#Output: 'anshu'

" An shu ".strip()
#Output: 'An shu' 

NOTE: we can define our own delimitor also: 

"anshuman".strip("an")
#Output: 'shum'

LSTRIP and RSTRIP FUNCTION: lstrip removes the delimitor from the left side,
rstrip removes the delimitor from the right side

"0002000".lstrip("0") #Output: '2000'
"0002000".rstrip("0") #Output: '0002'

STARTSWITH and ENDSWITH FUNCTION: checks if the string starts with or ends with a 
particular character, please note that it is a case sensitive function.

"anshuman".startswith("an") #Output: True
"rutu".endswith("tu") #Output: True

USE CASE: can help you have generalized user input in your if/else code, eg: 

"aDdiTion".lower().startswith("add") #Output: True 

REMOVEPREFIX and REMOVESUFFIX FUNCTION: works exactly the same as lstrip and rstrip, respectively

FIND FUNCTION: works exactly the same as the index function and gives you the first occurence

ZFILL FUNCTION: fills number of zero on the left side till total characters
become as many as n.

"10".zfill(5) #Output: '00010' NOTE: filled 3 zeros only because n = 5

SWAPCASE FUNCTION: makes uppercase character lower and lowercase character upper

"aNsHuMaN".swapcase() #Output: 'AnShUmAn'

LJUST and RJUST FUNCTION: used to l-justify or r-justify, helps add space

REPLACE FUNCTION: 

"anshuman".replace("an", "rutu") #Output: 'rutushumrutu'
NOTE: write what to search first and then write what to replace it with

JOIN FUNCTION: works the opposite as split function, where it takes a 
list output and turns it into a string (split function does the exact opposite).

NOTE: there is no default delimitor in this function and the delimitor 
needs to be the list name. 

bla = "Anshuman is Teaching Python".split() 
"".join(bla)
or 
bla = ['Anshuman', 'is', 'Teaching', 'Python']
"".join(bla)

#Both will give the same output: 'AnshumanisTeachingPython'

EXAMPLE: 

bla = "Anshuman is Teaching Python"
res = bla.split() #Output: ['Anshuman', 'is', 'teaching', 'Python']
res[2][::-1] #Output: gnihcaeT

res[2] = res[2][::-1] 
" ".join(res)
'Anshuman is gnihcaeT Python'

---
EXERCISE: How do you examine a list and see if there are repetitive 
elements or not? 

FIRST APPROACH: 

blah = [10, 20, 30, 10, 40]
bla = blah.sort()
for i in range(len(bla)):
    if bla[i] == bla[i+1]:
        print("Your list has repition")
    else: 
        print("Your list is unique")

ALTERNATIVE APPROACH: 

for idx, item in enumerate(blah):
    if item in blah[idx+1:]:
        print("Your list has repition")
    else: 
        print("Your list is unique")