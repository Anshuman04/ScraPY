PRINT FUNCTION: 
print("hello world") #double quote is the safest
print('hello world') #can use single quote as well
print("anshuman's world") #using double quote to print single quote
print('anshuman said "how are you?"') #using single quote to print double quote

#how to enter the python interpretor: python
#how to exit the python interpretor: exit()

#how to print a sentence with both double quote and single quote:
"""you can use \ to make python understand the second meaning of anything,
see example below"""
print("\"how are you?\" sounds sexy in Anshuman's voice")

#how to print a sentence in two lines: using n
print("first line \n second line")

#how to print a sentence with a tab space: using t
print("anshuman \t gaharwar")

VARIABLES:
Integer (int): 0,1,2,3,-1,-2,-3,240
Float (float): 0.1, 10.7, 3.1434567876, -3.6751
String (str): "Hello", 'Anshuman', "123", '3.14'
----
Boolean (bool): True, False #note: True = 1 and False = 0 in all languages 
None (NoneType): None
----
Eg: var = 1
How to check type? type(var)
How to do type casting? float(var); str(var); int(var)
#note: never use bool and nonetype for type casting or conversion 

AIRTHMATIC OPERATIONS: +, -, *, /, %, //, **
+ = summation
- = substraction
* = multiplication
/ = division (gives decimal output) #eg: 21/5 = 4.2
// = division (gives quotient) #eg: 21/5 = 4
% = division (gives remainder) #eg: 21/5 = 1
** = to the power #x to the power 1 or x^1 or x**1

LOGICAL OPERATIONS: and, or (gives output always as either true or false), not 
#and: both input must be true for the output to be true
#or: atleast one input should be true for the output to be true
#not: toggle function 

"""note: if there is a True event before "OR", it will give output true without even looking at the second event. Same
can be applied to a False event before "AND", and will give output false in that case cause it will not even go to evaluate 
the second event"""

FORMAT PRINING: 
print(f"your value was {}") #directly printing the variable 
print(f"your value was {var} with type as {type(var)}") #calling a function and printing the output
print(f"sum of 10 and 20 is {10 + 20}") #evaluating an algebraic expression 

ASSIGNMENT OPERATOR: = 

INPUT PRINT: #helps python get an user input such as username or age etc
name = input("Enter your name: ") #note: input function has the same format as the print function but it makes python stop and get user input instead of moving onto the next line directly
#note: eerything that comes from input function is a string and if were expecting an integer or float then you need to type cast it separately, eg:
age = int(input("Enter your age: "))

COMPARATERS: ==, !=, <, >, <=, >= #note: gives output in the form of true or false
2 < 3 #True
2 > 3 #False
2 <= 2 #True
5 >= 7 #False
2 == 2 #True [note: == means are the two terms same]
2 + 2 == 1 + 3 #True
2 + 2 * 2 == 1 + 3 * 2 #False [note: since BODMAS is applied]
(2+2)*2 == (1+3)*2 #True
2 != 3 #True [note: != means are the two terms not the same]