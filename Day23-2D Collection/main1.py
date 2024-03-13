groceries=[["apple","orange","banana","coconut"],["celery","carrots","potatoes"],["chicken","fish","turkey"]]

print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries) 
print(groceries[0][1]) #orange
print(groceries[0][2]) #banana
print(groceries[2][1]) #fish

print()
print("-----Loop-----")
print()

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

groceries=({"apple","orange","banana","coconut"},{"celery","carrots","potatoes"},{"chicken","fish","turkey"})

print()
print("-----Loop-----")
print()

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()