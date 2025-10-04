"""
Functions - to break a very long piece of code into parts
"""

"""
def <function name> ():
    <some code block>
    <some more>
    return <Any datatype> # Defaults to None

def function will define a function, python will skip this when it encounters. It wil run this code block only when we call it.
"""

def get_custom_greeting(name):
    print("Hello from Anshuman")
    return f"Hello {name}"

print("I am teaching functions")
result = get_custom_greeting("Rutu")
print(f"CLass is done: {result}")


def take_multiple_numbers(nums):
    result = []
    for i in range(nums):
        x = int(input("Enter a number: "))
        result.append(x)
    return result

bla = take_multiple_numbers(2)
print(bla)
hihi = take_multiple_numbers(3)
print(hihi)


"""
You can call functions from different files/folders:
Approach 1: File in same folder: from <file name> import <function_1>, <function_2>
Approach 2: File in different folder: from <copy relative path, replace slash with <.>, <error for .py or any other file extension>> import <function> # The logic is the same

Approach 2: is preferred option
"""






