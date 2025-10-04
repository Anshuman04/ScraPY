FUNCTIONS: used for making the lines of your code shorter

SYNTAX: 
def <function_name>(): #this is the input
    <Some code block>
    <Some more>
    return <variable_name> #without this it'll default to none

Eg:

def take_multiple_numbers(nums):
    result = []
    for num in nums: 
        result.append(int(input(f"enter number {num}: ")))
    return result

Elaboration: 

def take_multiple_numbers(nums):
    result = []
    for i in range(nums):
        x = int(input("Enter a number: "))
        result.append(x)
    return result 

bla = take_multiple_numbers()
#Output: 
"""Enter a number will keep showing up the same number of times equal to the value of #nums"""

i.e.,
bla = take_multiple_numbers(2)
#Output: 
Enter a number: 4
Enter a number: 5

print(bla)
#Output: 
[4, 5]

"""Can also make a separate file out of the function lines, where these subfiles should
all be in the same folder"""

SYNTAX TO CALL THE FILE:

from <file name> import <function1, function2, function3>

NOTE: always write this line in the very beginning of your code

"""Can also make a separate file out of the function lines, where these subfiles are
not present in the same folder"""

SYNTAX TO CALL THE FILE: 
#copy relative path: practice\root2\functions_classwork.py
from <copy relative path> import <function1, function2, function3> #preferred way

i.e.,
from practice.root2.functions_classwork import take_multiple_numbers

