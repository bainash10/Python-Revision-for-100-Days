 # * collection = single "variable" used to store multiple values
# * List  = [] ordered and changeable. Duplicates OK
# * Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# * Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple","orange","banana","coconut"]
print(fruits)   #['apple', 'orange', 'banana', 'coconut'] --> output

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])


print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])
print(fruits[1:3:1])


print("---looping---")
for x in fruits:
    print(x)



