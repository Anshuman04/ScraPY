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

name = input("Enter your name: ")
print(f"Welcome {name} to the world of calculator!")

choice = 0
while choice < 5:
    
    print("What do you want to do today? \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")
    choice = int(input("Enter your number of choice from the above: "))
  
    if choice == 5:
        print("\n  Thank you for choosing my calculator!")
        break

    elif 0<choice<5:
        first_num = int(input("Enter first number: "))
        second_num = int(input("Enter second number: "))

    else:
        print("\n Invalid choice, choose again!")
        choice = 0
        continue
    
    if choice == 1:
        result = first_num + second_num
        print(f"Addition of {first_num} and {second_num} gives {result}.")

    elif choice == 2:
        result = first_num - second_num
        print(f"Subtracting {second_num} from {first_num} gives {result}")

    elif choice == 3: 
        result = first_num * second_num
        print(f"Multiplying {first_num} with {second_num} gives {result}")

    elif choice == 4:
        if second_num != 0:
            quotient = first_num // second_num
            remainder = first_num % second_num
            print(f"Dividing {first_num} by {second_num} gives quotient as {quotient} and reminder as {remainder}.")
        else:
            print("Division by 0 is not allowed")
            continue
    
    #print(f"Btw, Your addition was {first_num + second_num} and division is {quotient} Lets do more calculations")
    
   

   


