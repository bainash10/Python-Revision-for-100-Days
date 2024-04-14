
#* Below is the example of program without using walrus operator
# foods =list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append


#* Below is the example of program using walrus operator
foods=list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)