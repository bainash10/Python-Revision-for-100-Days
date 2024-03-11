 # * collection = single "variable" used to store multiple values
# * List  = [] ordered and changeable. Duplicates OK
# * Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# * Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = {"apple","orange","banana","coconut"}

print(fruits)

# print(dir(fruits))  #shows what are the operations(attributes and methods) that can be performed

# print(help(fruits)) #to get help in using operations of sets

print(f"The length of the list is: {len(fruits)}") #gives the length of the sets

print("apple" in fruits) #Returns if apple lies in the sets fruits or not --> returns true

print("pineapple" in fruits) #Returns if apple lies in the sets fruits or not --> returns false

# print(fruits[0]) --> cant be done 
# NOTE:Cannot change a value of sets but can remove or add other elements

fruits.add("pineapple")
print(fruits)

fruits.remove("apple") #remove the specified element
print(fruits)

fruits.pop() #removes the first element in an set but will be random, random because sets are unordered collection of values
print(fruits)


# fruits.clear() #prints --> set()
# print(fruits)

fruits2 = {"apple","orange","banana","coconut","coconut"}
print(fruits2)  #In set no duplicates should be present so it will print only one coconut instead of two


print("***They are iterable***")
for z in fruits2: 
    print(z)