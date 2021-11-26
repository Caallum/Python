import os

def callum():
    print("This is a predefined function!")

    # The 'print' function is a predefined function, that displays text into the console. Above is an example usage of the print function.

#
#
def sam():
    # Task: Display the sentence: "Hello World!" without any errors when running

    return


user = input("Sam or Callum? (S/C) ")
if user == 'c' or user == 'C':
    os.system("cls" if os.name == "nt" else "clear")
    callum()
elif user == 's' or user == 'S':
    sam()
else:
    print("Invalid user")