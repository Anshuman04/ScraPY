# stars = int(input("number of stars: "))  
# square = "*" * stars 
# print(f"{square} \n" * stars)

#print("--|  |------|  |----")

nix = input("enter first option: ")
#nix == "True"
v3 = nix == "True"

niki = input("enter second option: ")
# niki == "True"
v4 = niki == "True"

# print(f"i/p --|{v3 * "--"}|------|{v4 * "--"}|---- o/p")  

# print("\n")

# print(f"      |{v3 * "--"}|      \ni/p---|{v4 * "--"}|---o/p")

#rint(f"i/p --|{v3 * "--"}|-------|{v4 * "--"}|----- o/p  \n \n       |{v3 * "--"}|      \n i/p---|{v4 * "--"}|---o/p ")

print(f'i/p--|{(int(v3) * "--") + (int(not v3) * "  ")}|-----------|{(int(v4)* "--") + (int(not v4)* "  ")}|----o/p')

print("/n")



print(f'         |{(int(v3) * "--") + (int(not v3) * "  ")}|       \n i/p-----|{(int(v4)* "--") + (int(not v4)* "  ")}|------o/p')