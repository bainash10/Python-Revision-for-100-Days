 #* Nested Loop: A loop within another loop (outer, inner)
#* Outer loop:
#*      Inner Loop: 

for i in range(1,11):
    print(i, end="") #will print on the same line 

print("\nNew example 1")
for i in range(1,11):
    print(i, end="") #will print on the same line with - in between the numbers

print("\nNew example 2")
for x in range(3):
    for y in range(1,4):
        print(y, end=" ")
    print() #prints a new line