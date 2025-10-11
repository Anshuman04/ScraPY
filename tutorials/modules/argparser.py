import argparse

def greet(name):
    print(f"Hello, {name}!")

def am_i_old(age):
    if age > 18:
        print("You are old")
    else:
        print("You are not old")

parser = argparse.ArgumentParser()
parser.add_argument('--name', default="Anshuman", help="Enter your name")
parser.add_argument("--age", type=int, required=True, help="Enter your age")
parser.add_argument("--debug", default=False, action="store_true", help="Enable debug mode")
# parser.add_argument("--surname", dest="last_name")  # dest ke andar thusega

allArgs = parser.parse_args()

# import pdb; pdb.set_trace()
greet(allArgs.name)
am_i_old(allArgs.age)
# print(allArgs.flag)

if allArgs.debug:
    print("Debug mode is on")
    print(allArgs)
