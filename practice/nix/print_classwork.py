# double quote print usage
print ("Learning python")

#single quote can also be used 
print ('Iam learning python')

#use single quote if you want to print double quote as part of a string and vice versa
print ('Anshuman said: "Share your screen"')

"""
if you are using both single and double quote as part of your string then put a backslash '\' before the quote 
to make python take the second meaning of the quote.
"""
print('Anshuman\'s asking to share screen again')
print("Anshuman said; \"Hey\"")

#to print multiple lines use '\n'. it takes the second meaning of n which is to print on the next line.
print('hello\n world')

# '\t' gives a tab space between words
print ("anshuman wants \t to go ahead")

"""
There are 5 types of variables; integer, string, float, boolean, NoneType
Integer (int): any number without decimals. 0, 1 ,2 , -11
Float (float): any numbers with decimals, 0.1, 0.5, 3.5434, -6.46
string (str): any set of characters in between double or single quotes. "hello", "120" 
Boolean (bool): True or False. Basically 0 or 1. Note it starts with capital letter. True. its not true.
NoneType(None): kuch nahi. only way to write is None. first letter is capital dont change it idiot.
"""
var1 = 123
var2 = 3.14
var3 = "0110"
var4 = True
var5 = None
var6 = "Nix"

# you can define these variables and check their type by using the type('varibale name') command
print(type(var2))

#you can convert one variable type to another if its acceptable in the type, this is typecasting. for example, var1 can be converted to str
print(str(var1))  #int to str

# print(float(var6)) this cant be executed because var6 is a string so float can't convert it into a float because its not of base 10 (decimal)
# if its a valid string like '123' float and int will convert them accordingly

print(float(var1))  #int to float vice versa is also acceptable

print(float(var3))  #str to float
print(str(var4))  #bool to str. 

print(bool(var6)) # any string will give you true

# if you typecast float to an int, it just takes the nos before the decimal. if you want to round use the round function.


"""
There are different arithmetic operations; +, -. *. /. //. %, **
you can use these operators on same type of variables. 
python can also add two strings, one float and one int, True + 2, or True + 2.0 (here python takes True as 1)
cannot subtract 2 srings, but you can subtract one float and one int, or True - 2. 
you cannot divide two strings. if you divide int by int, it will give you a float. 
double divide (//) will give you just the quotient. 
modulus divide (%) will give you the remainder
you cannot multiply two strings. but you can multiply one string with a int not with a float though. 
** means power of. 3**3 =27, 2**2 = 4, 6**2 =36
"""

"""
Logical Operations: and, or not
1. or: think of it as a parallel circuit connection.
        True or Flase / False or True will give True
        True or True = True
        False or False = False

2. and: its a series circuit connection
        True and True = True
        True and False / False and True = False
        False and False = False

3. not: not toggles the input, basically switch kar deta hai.
        not True = False
        not False = True
"""
v1 = 12
v2 = "nix"
v3 = 3.14
v4 = True

# format printing. 

print(f"Your variable is {v1}, whose type is {type(v1)}")
print(f"Your varibale is {v2}, whose type is {type(v2)}")
print(f"printing varibale {v3}")
print(f"printing after calculation {v1+v3}")
print(f'printing type {type(v4)}')

# input from user. input hamesha string hota hai
name = input("Enter your name: ")  #quote ke beech wali cheez print hogi aur user ke input ka wait bhi karega
print(name)

#another way to do this is:
print(f"Hello, {name}!")

#input will be string. so makesure to typecase if you want to do some arithmetic operations on them
age = input("Whats your age? ")
# age + 2 will give error, so type cast it
real_age = int(age)
real_age = real_age + 5
print(real_age)

#assignment operator (=): right side ki value ko left side variable name pe assign kar dega
age = 25
age = age + 10
print(age)  #yahan 35 print hoga

#comaprison operators: kya lagake socho? output hamesha boolean mein aayega, True or False
"""
2 == 2 True
2 != 3 True
2 > 4 False
2 <= 4 True
"""

