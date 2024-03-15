#dictionary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates

capitals={"USA":"Washington D.C.",
          "India":"New Delhi",
          "Nepal":"kathmandu",}

# print(dir(capitals)) #prints all methods and attributes related to dictionaries
# print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("India"))
print(capitals.get("Nepal"))
print(capitals.get("NEpal")) #shows None as case sensitive
print(capitals.get("Japan")) #shows None as it is not in dictionary

if capitals.get("Nepal"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany":"Berlin"}) #will add new item in dictionary i.e at the end of the dictionary
capitals.update({"China":"Beijing"})
print(capitals)

capitals.pop("China") #It pops out the China from the dictionary

capitals.popitem()  #doesnot required to pass key, it simply removes the last added item
print(capitals)


# capitals.clear() #clears the dicitonary and prints{}

keys=capitals.keys()  
print(keys)  #Provides all the keys as: dict_keys(['USA', 'India', 'Nepal'])

for key in capitals.keys():
    print(key, end=" ")   #prints: USA India Nepal
print()

values= capitals.values()
print(values)  #prints: dict_values(['Washington D.C.', 'New Delhi', 'kathmandu'])


values= capitals.values()
for value in capitals.values():
    print(value,end=" ")  #prints: Washington D.C. New Delhi kathmandu
print()

items=capitals.items()
print(items)  #prints= dict_items([('USA', 'Washington D.C.'), ('India', 'New Delhi'), ('Nepal', 'kathmandu')])
#it prints as [(),(),()]

items=capitals.items()

for key,value in items:
    print(f"{key}: {value}") 
    # o/p will be as follows: 
    # USA: Washington D.C.
    # India: New Delhi
    # Nepal: kathmandu