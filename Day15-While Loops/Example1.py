age = int(input("Enter your age: "))

while age < 0:
    print("Age cant be negative")
    age = int(input("Enter your age: ")) #If not kept this it will be a infinite loop

print(f"You are {age} years old")