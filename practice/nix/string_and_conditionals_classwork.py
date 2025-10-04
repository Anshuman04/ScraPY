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
you can directly type the data structure itself. like dir(str), dir(""), dir(int), dir(10), dir(list), dir([])
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

if i want to print form right to left
name[::-1]  this will print the entire string in reverse
"""

#STRINGS ARE CASE-SENSITIVE!!!!!

"""
String is a collection of characters
List is a collection of any data structures.

A container can refer to a list or string.

blank list looks like this, 
v1 =[]
"""

v3 = [ 10, 20, 30, 40, 50]  #---> this is a collection of integers. each element is an integer.
print(v3[2])        # here you are trying to address the element. 
print(v3[2:])     # to access each element the syntax is similar to aceessing characters in a string. : means you are trying to slice
print(v3[::-1])   # this will print the entire list in reverse

"""
--> len (Length): This is a function that works both on strings and list
iut wont work on integer. matlab agar ek variable = an integer. aur uska length nikalne ka try karoge toh kuch nahi aayega

len(v3)  
"""
# we can edit a container. we can change the elements in a list

v3[2] = 35
print(v3)     # this type of assignment or editing won't work on a string.

# to add things to a list, we will use the 'append' function.

v3.append(80)
print(v3)

# you can add anything inside a list. a list can have strings, int, float, bool, none, another list all at the same time.

other_list = [1, 2, 3]
v3.append(other_list)
print(v3)      # this will print the entire list with [] inside v3

# but if i want the other_list in v2 but just the elements and not as a string

#EXTEND
v3.extend(other_list)
print(v3)

a = [10, 20 , 30]


#INSERT: you can insert anything into a list. if you insert a list in between it will get added with []. you can not add individual elements with insert command
a.insert(2, 25)
print(a) 


# REMOVE: it removes something from a list literally

a.remove(25)
print(a)   # remove normally removes the first occurance of the element in a list.

#POP
queue = ["Anshu", "Manav", " Rutu", "Nix"]
processing = []

# name = queue.remove("Anshu")  ---> the variable name won't print anythng because the remove command wont return anything. it jsut takes it and throws it away

# but pop extracts and returns the value. it removes and returns the item at an index. 

name = queue.pop(0)
print(name)

processing.append(name)  #when you print this it will give anshu 

# it defaults last. that means if you just write queue.pop() wuthout an index, it will just pop the last element
# clear removes everything from a list and gives an empty list

"""
-->COUNT:
 this counts the number of particular element in a list
 b = [ 1,2,3,4,5,6,6,6,7,7]
 b.count(6)   this iwll give how many 6 are present in the list

 NOTE: if you want to remove the 6 present in index 6, then use pop instead of remove as remove will just take out the first 6, that is index 5

"""
"""
--> INDEX: this is used to search the index of a particular element
b.index(2)
 if i want to access the index of 6, it wil just tell me the index of the first 6. (stupid but ok)

"""
"""
--> REVERSE: this will literally reverse the list
bla = [1 ,2, 3, 4, 5, 6, 7]
blah.reverse()

you can use the indexing method to rewverse also, i.e reve_bla = bla[::-1]
but this wont change the original bla, so if you dont want to change the original order, use this method. If not just use the .reverse function

"""

"""
--> SORT: 
var = [20, 4, 89, 39, 90, 33, 8]
var.sort()  this will by default sort in ascending order.

var.sort(reverse=True)  this will sort in descending order

--> you can delete some consecutive elements via slicing and then adding

v1 = [1,2,3,4,5,6,7]
v1[0:2]    This will give [1,2]
v1[4:]     This will give [5,6,7]

v2 = v1[0:2] + v1[4:]

This will gie [1,2,5,6,7]

"""

"""
--> CLASS EXERCISE:

var = [10, 20, 30, 40, 50, 20, 10, 40, 50, 60]
num = input("Enter a number: ")

Delete the second occurance of that number and print the remaining list
also try deleting the thrid occuranc of a number
"""

"""
INBUILT FUNCTIONS OF STRINGS: 

1. Count will give you the number of a particular character or item in a string or list respectively. 
[10,20,30,10].count(10) ----> This will give you 2 as the output
"Anshuman".count("an") ----> 1

count is case sensitive, which is why the first An is not considered

2. INDEX: index will give the position of the particular character in a string. It will give the first occurance of the character/substring
    If you give multiple characters (substring), it will tell you from which position the character starts from. 

3. ISUPPER / ISLOWER : Checks if all characters of a string is upper or lower case and gives the output in Boolean (True or False)
    "anshu".islower() ---> True
    SInce it gives output in bool, its a conditional, so you can use it against if/else statement
    to check a particular character, you need to fist access the particular character and then check
    EG: "aNshu"[1]  this is acessing 'N"
    so now you can do "aNshu"[1].isupper() ----> This will give True

4. IsTITLE: It checks if a word has first letter is uppercase and other case are lowercase. 
    "Anshuman".istitle() -----> True
    "Anshu Is Teacher".istitle() -----> True

5. isDIGIT: Checks if all characters in a string are digits
    "23".isdigit() ----> True
    "23.2".isdigit() ----> False    This is because there is a dot in between the string. 

6. isALNUM: Is a string alpha-numeric. Can be used to check usernames dont have special characters
    "anshu".isalnum() --->True
    "Anshu".isalnum() ---> True
    "anshu07".isalnum() ----> True
    "anshu007$".isalnum() ----> False
    _ is not a alphabet for string. It is however a alphabet in case of variable name and can be used. like var_2 = 10 is acceptable but var$2 =10 is not acceptable
    so here "anshu_07".isalnum() ----> False

7. isALPHA: this checks if the characters are all alphabets:
    "anshu".isalpha() ----> True
    "aNshu".isalpha() ---> True
    "anshu07".isalpha() ----> False

8. Lower/Upper:  Lower will convert the entire string to lowercase and upper will do the opposite
    "Anshu".lower() ----> 'anshu'
    "ANSHU".lower() ----> 'anshu'
    "anshu".lower()----- 'anshu'
    "anshu".upper() ----> ANSHU

Example usecase; Incase of calulator program where I want add, Add, ADD, everythin to work I can do the following
    bla = "ADD"
    bla.lower() == "add"  ------> this is converting bla to all lower case and the checking if its equal to 'add' which is true. so now this has become a conditional and can be used in an if statement

    In general lower and upper functions are nto conditionals, so it cant be directly used in a an if statement, but it can be combined with a conditional operator like ==, <,>. != and can be used as a condtional.

9. SPLIT: 
    bla = "Anshuman is teaching"
    result = bla.split() -----> ["Anshuman", "is", "teaching"]
    type(result) ----> list

    It splits a string and returns the output in the form of list. Now you can use the funtions of list on the output
    foor example: 
        bla.split().pop(0) -----> Anshuman   pop(0) gave the output as a string by taking the first element in the list
        bla.split().pop(0).upper()  -----> ANSHUMAN

    split bydefault splits the string at spaces. This cutting process is callled delimiting. The character at which its cutting(space) is called delimiter
    You can delimit using any character and tell it. 

    var = "Anshuman_Gaharwar_22987_30"

    here is you use var.split it wont dplit anything
    but you can change the delimiter,
    var.split("_") -----> This will split the string at the delimiter.

    Remember that the delimiter wont be a part of the output list. 

SOPME TOOFANI USECASE SHOWN BY GURUJI:

bla = ["Anshuman_Gaharwar_22987_30", "Rutu_Mishra_160401_27"]
for person in bla:
    first_name, second_name, employee_id, age = person.split("_")
    print("="*40)
    print(f"First name: {first_name}")
    print(f"Second name: {second_name}")
    print(f"Employee id: {employee_id}")
    print(f"Age: {age}")

novel = "this is first line.\nThis is second line"
sentences = novel.split("\n")
This will return 
['This is first line', 'This is second line']

YOU CAN ALSO USE MULTIPLE CHARACTERS AS DELIMITERS
for example:
"anshuman loves chocolate and icecream.".split("an")

This will return ['', 'shum', 'loves chocolate', 'd icecream.']    ----> Since it encountered 'an' in the start of the string only, the first is an empty string
the internal working is like, it makes an empty list, and ten makes an item (empty string) on it, then goes to check the string. since the first character itself is a delimiter its like 'ok i need to take out this and go ahead so it leaves behind an empty string and then goes to shum'

10. splitlines 
    this will split the string with default separator as \n

    so you can do novel.splitlines() for the above example

11. STRIP:
    it will remove spaces form a string.
    " anshu  ".strip() == "anshu" ----> True
 by default it strips spaces because that is the default delimiter.
 you can give a limiter to strip aslo, 
 "anshuman".strip("an")  -----> 'shum'
 "02".strip("0") -----> '2'

 12. lstrip/rstrip: left strip or right strip
    "000200".lstrip("0")  ----> '200' 
    similar for rstrip it will strip only from right sides

STRIPS WILL ONLY REMOVE DELIMITERS FROM THE SIDES, NOT FROM BETWEEN VALID CHARACTERS!!!

    "  A N S H U   ".strip()
    This will give: 'A N S H U'

13. startswith / endswith: It checks if the string starts or ends with particular character and return True or False. SO can be used with if statements
    "anshu".startswith("an") ----> True

    EXAMPLE: 
    bla = "add"
    bla.startswith("add") ---> True
    "addition".startswith("add") ----> True
    "addITION".lower().startswith("add") ---> True

    Now this will make the code genralized where whatever the user types for addtion it will be accepted. 

14. removeprefix / removesuffix: Same as lstrip and rstrip. Guruji ne khud pichle 10 saalon mei use nahi kiya hai toh dekhlo 

15. Find: Its same as index. Gives the first occurance.  
    There is something called lfind, it will search from the right side and gives the first occurance, which is basically your last occurance. 
    SImilarly there is an rindex also. 

16. ZFILL: Fills 0 in a string
    x = "10"
    y = "200"
    x.zfill(4) ----> 0010
    y.zfil(4) -----> 0200

It will fill 0's till the total number of characters becomes equal to the number given in the ()

17. swapcase: it changes lower to uppencase and viceversa
    "AnShuman".swapcase() -----> aNsHUMAN

18. ljust / rjust: justifies strings to left or right

    "Anshu".rjust(10) -----> "     Anshu"    Adds spaces till the toal character is 10 and word is ending at the right

    bla = ["Anshuman", "Rajasthan", "Constellation"]
    result =[]
    for item in bla:
        result.append(item.rjust(20)]
    for item in result: 
        print(item)

    OUTPUT:
                    Anshu
                Rajasthan
            Constellation

Basically i fixed 20 characters in a line and adjusted all the string to the right. 

19. Replace:  replaces characters in a string. its searching for soemthing and replacing it with another
    'anshuman'.replace("an", "rutu")  -----> 'rutushumrutu'

20. Join: Takes a list as input and gives out a string. Kind of opposite as strip where it takes a string and returns a list. 
    It does not give a by default separator. 
    syntax is a little different

    bla = ['anshu', 'is', 'teaching']
    "*".join(bla)  ----> anshu*is*teaching
    " ".join(bla) ----> anshu is teaching '

    example:

    bla = "anshuman is teaching python"
    res = bla.split()
    res[2][::-1] ------> gnihcaet          # here we are basicallu reversing the 3rd element and replacing it in the original list in the next line
    res[2] = res[2][::-1]
    " ".join(res) -----> 'anshuman is gnihcaet python' 


"""


list = [10, 20 , 30, 30]
res = []
for item in list:
    res.append(item)
    print(res)
for i in range(len(res)):
    if res[i] == res[i-1]:
        print("Not unique")

    else:
        print("Unique")



