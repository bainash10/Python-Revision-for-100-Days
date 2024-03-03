email=input("ENTER YOUR EMAIL: ")
index=email.index("@") #returns the index of @
print(f"The index of @ is {index}")

username = email[:index]
domain = email[index+1:]
print(f"Your username is {username} and domain is {domain}")