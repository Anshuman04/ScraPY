"""
if-else
"""
# if <condition>:         # Agar ye condition true hai       # Can be any comparator
    # <if block>          # to ye
# else:                   # nahi to
    # <else block>        # ye
if True:
    print("I am if block")
else:
    print("I am else block")

if True == False:
    print("I am printing if block")
else:
    print("I am printing else block")


"""
use of elif
"""
baarish = True
go_out = True
if baarish and go_out:
    print("Get your umbrella. Its gonna rain")
elif baarish and not go_out:
    print("Chup chap baith ghar mein")
elif not baarish and go_out:
    print("Bindaas bahar jaa")
else:
    print("WTF?? khud soch le")
# Note: Any output that gives a bool output (True, False) can be used in if-else
num = int(input("Enter your number: "))
if num < 3:
    print("Your number is less than 3")
else:
    print("Your number is not less than 3")



"""
Member operators - is, in
"""
# is kya left condition right condition mein hai?
# in kya left condition right condition mein hai?
if "Anshu" in "Anshuman":
    print("Search found")
else:
    print("Search not found")


var1 = 0
var2 = 1
if var1:
    print("Success")
if var2:
    print("Success") # All number will be true, including decimal except 0
if -2:
    print("Success")
if "Anshu":
    print("Success") # All strin will be true, except ""
if None:
    (print"HAHA") 
if not None:
    print("HAHA")


# Example to use not something
num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))
if not den:
    print("Denominator cannot be zero")
    exit()
print(f"Quotient: (num//den)")


"""
Self learning tools
"""
var1 = 10
var2 = "Anshu"
print(dir(var2))
print(var2.count.__doc__) # can be any function instead of count


"""
Indexing
"""
name = "ANSHUMAN"
name[0]
name[1] # and so on, only integers, negative is okay


"""
Slicing
"""
# syntax --> <variable name>[<start_idx>:<end_idx>]
# remember start_idx is inclusive and enx_idx is non-inclusive (so always add+1) 
gene = "XYZ1"
gene[0:3]
# can also skip
# syntax --> <variable name>[<start_idx>:<end_idx>:<step_size>]
name = "ANSHUMAN"
name[0:8:2] # Print every second character
name[::2] # Start from start, end at end, take every second character


# slicing with negative integers
#  A  N  S  H  U  M  A  N
#  0  1  2  3  4  5  6  7
# -8 -7 -6 -5 -4 -3 -2 -1

name[-1]
name[2:] # take everything from this indexed character
name[:5] # take everyting until this indexed character
name[::-1] # to print in reverse
name[-3:-7:-1]
# Strings are case sensitive
name = "Anshuman Gaharwar"
name[6] = name[10] # True
name[6] = name[0] # False


"""
Lists
"""
# List - A collection of data structures
# syntax to declare a blank list: var1 = []
                                # type(var1)
# List is a type of variable.
var2 = [10, 20, 30, 40, 50]
type(var2)
type(var2[0]) # to check the element within the list
var2[0]
var2[-2] # negative numbers work
var2[2:] # slicing works
var2[::-1] # reverse works

# Slicing vs addressing == : vs <idx number>

# function called len which stands for length
# works on strings, lists and dictionary
# will not work on int and float
len(var2) # 5 elements in the variable var2
len.__doc__

# To edit specific idx in a list
# Change 30 to 35 in var2
var2
var2[2]
var2[2] = 35
var2
# This kind of assignment does not work with strings as there is a funciton in str to do this
bla = "Anshu"
bla[0] = "A"

# To add a new element using append function
var2[5] = 60 # Will not run as the list assignment index out of range
print(dir(var2))
print([].append.__doc__) # Append object to the end of the list
var2.append(90)
var2
var2.append("Anshuman")
var2.append(3.14)
var2.append(True)
var2.append(None)
other_list = [1,2,3]
var2.append(other_list)
var2 # It will add all type of variables to a list
var2 = [10, 20, 30]

# Use of extend function
var2.append(other_list) # or
var2 = [10, 20, 30]
var2.append(1) # and so on until the end
var2 = [10, 20, 30]
# But if list to add is too long, then how to do it?
var2.extend(other_list)

# Use of insert function - How to add things in between your variable
print([].insert.__doc__) # Insert object before index
# Add 24 before 30
var2.insert(2, 25) # syntax: <variable>.insert(<index position>, <object>)
var2

# Use of remove function
var2.remove.__doc__ # Remove first occurrence of value. Raises ValueError if the value is not present.
var2.remove(25)
# But what if you want to remove second occurence?
# Cant remove multiple element in one go
var2 = [10, 20, 30, 1, 2, 3, 30]
var2.remove(10, 20) # ERROR: list.remove() takes exactly one argument (2 given)


# Use of pop function
queue = ["Anshuman", "Manav", "Rutu", "Nix"]
processing =[]
name = queue.remove("Anshuman")
name # no results as remove results in loss
queue
print([].pop.__doc__) #Remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.
name = queue.pop(0)
processing.append(name)
processing
queue
# pop basically removes and allows for retrieving the element
var = [1,2,3,4,5]
var.pop()
var
var.pop(7) # out of range
processing.append(var.pop(0))
var
processing

# use of reverse
bla = [1,2,3,4,5]
bla[::-1] # slicing method
bla # print as was defined. Thus, this approach does not cause loss of original defined variable  
bla = [1,2,3,4,5]
bla.reverse()
bla # the original defined variable is overwritten and lost
 

# use of clear function - to clear the list
var2.clear()
var2
var = [1,2,3,4,5]
var = [] # alternative method

# use of count function
var = [1,2,3,0,4,5,0,6,0,7]
var.count(0)

# use of index function - a searching function
print([].index.__doc__) # Return first index of value. Raises ValueError if the value is not present.
var = [10,20,30,40]
var.index(30)
var[2]

# Use of sort function
print([].sort.__doc__)
hihi = [20,1, 0, 8, 75, 33]
hihi.sort() # default is ascending
hihi = [20,1, 0, 8, 75, 33]
hihi.sort(reverse = True)

# To delete consecutive things using slicing
hihi[0:2]
hihi[4:]
hihi[0:2] + hihi[4:]
q = [1,2,3,4,5,6,7,8,9,10]
x, y = q[::2], q[1::2]
x
y

"""
Exercise problem:
var = [10, 20, 30, 40, 50, 20, 10, 40, 50, 60, 10]
num = int(input("Enter a number: "))

Delete second occurence of that number and print the remaining list
"""
var = [10, 20, 30, 40, 50, 20, 10, 40, 50, 60, 10]
num = int(input("Enter a number: "))

left = var[:var.index(num) + 1]
right = var[var.index(num) + 1:]
right.pop(right.index(num))
print(var)
print(left + right)
