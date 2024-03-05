 #* While loop = Execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You didn't enter your name")
    name = input("Enter your name: ") #If not kept this it will be a infinite loop

print(f"Hello {name}")