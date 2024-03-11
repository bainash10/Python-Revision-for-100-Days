 # * collection = single "variable" used to store multiple values
# * List  = [] ordered and changeable. Duplicates OK
# * Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# * Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple","orange","banana","coconut","coconut")

# print(dir(fruits))  #shows what are the operations(attributes and methods) that can be performed

# print(help(fruits)) #to get help in using operations of tuples

print(f"The length of the list is: {len(fruits)}") #gives the length of the sets

print("apple" in fruits) #Returns if apple lies in the tuple fruits or not --> returns true

print("pineapple" in fruits) #Returns if apple lies in the tuple fruits or not --> returns false

print(fruits.index("apple"))

print(fruits.index("orange"))

print(fruits.count("coconut"))

print("***They are iterable***")
for z in fruits:
    print(z)