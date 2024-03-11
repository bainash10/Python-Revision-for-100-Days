 # * collection = single "variable" used to store multiple values
# * List  = [] ordered and changeable. Duplicates OK
# * Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# * Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple","orange","banana","coconut"]

# print(dir(fruits))  #shows what are the operations(attributes and methods) that can be performed

# print(help(fruits)) #to get help in using operations of lists

print(f"The length of the list is: {len(fruits)}") #gives the length of the list

print("apple" in fruits) #Returns if apple lies in the list fruits or not --> returns true

print("pineapple" in fruits) #Returns if apple lies in the list fruits or not --> returns false


print("---Replacing the element in list---")
fruits[0]="pineapple"
for fruit in fruits:
    print(fruit)

print("---Appending---")
fruits.append("guava") #['pineapple', 'orange', 'banana', 'coconut', 'guava'] --> O/p, NOTE: adds at the end of the list
print(fruits)


print("---Remove---")
fruits.remove("orange")
print(fruits) #['pineapple', 'banana', 'coconut', 'guava']

print("---Inserting in specific position---")
fruits.insert(0,"kiwi")
print(fruits) #['kiwi', 'pineapple', 'banana', 'coconut', 'guava']

print("---Sorting the list---")
fruits.sort() 
print(fruits) #['banana', 'coconut', 'guava', 'kiwi', 'pineapple']

print("---Reversing in the way list is initialized---")
fruits.reverse() #in reverse alphabetical order required then first sort in alphabetic order and sort
print(fruits) #['pineapple', 'kiwi', 'guava', 'coconut', 'banana']

#! print("---Clear the list elements---")
#! fruits.clear() #* []-->o/p
#! print(fruits) 

print("---Return Index of a value---")
a=fruits.index("banana") 
print(a)  #o/p-->4

print("---Couting---")
a=fruits.count("banana") 
print(fruits)  #o
