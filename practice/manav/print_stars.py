"""
 Exercise 1:
    Take input from user for number of stars
    Print sqaure full of stars with side length as input
    You can use only 1 print statement

If user has given 2, then output should be:
**
**

If user has given 3, then output should be:
***
***
***
"""

stars = int(input("Enter the number of stars: "))
print(f"{'*'*stars}\n"*stars)