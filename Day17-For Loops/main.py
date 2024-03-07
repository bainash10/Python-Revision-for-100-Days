 #* for loops = execute a block of code a fixed number of times.
#* You can interate over a range, string, sequence, etc.

for x in range(1,11): #Prints 1 to 10  #x can be named anything
    print(x)

print("This is outside the for loop")

for x in reversed(range(1,11)): #Prints 10 to 1 in reverse order  #x can be named anything
    print(x)

print("This is outside the for loop")

for x in range(1,11,2): #Prints 1 to 10  #step is 2
    print(x)


print("Example: Iterating over a string")
credit_card="1234-5467"
for x in credit_card:
    print(x)