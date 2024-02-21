# Variable = a reusable container for storing a value 
            # a variable behaves as if it were the value it contains

age = 12
print("age")
# print("You are"+age+"years old")   --> will show error so need typecasting

print("You are "+str(age)+" years old") 

print("You are",age,"years old") #when using comma spacing is automatically given by interpreter, typecasting is not required here

print(f"You are {age} years old")  #fstring
#Today we mostly use fstrings in our python program for printing statements


# assigning and printing the variables:

# Method 1:
x=1
y=2
z=3
print(x)
print(y)
print(z)

#Method 2:
x,y,z=1,2,3
print(x,y,z)  #prints all at once with space and horizontally

#Method 3:
x=y=z=0 #used for assiging coordinates of points with same values
print(x,y,z) #Prints 0 0 0 horizontally