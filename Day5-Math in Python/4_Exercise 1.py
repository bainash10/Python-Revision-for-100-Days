# Exercise name: Circumference of a circle
import math
radius =float(input("Enter the radius of a circle"))

circumference = 2* math.pi *radius

# print(f"The circumference is : round({circumference})") # prints the answer as: The circumference is : round(31.41592653589793)

print(f"The circumference is : {round(circumference,2)}") # Prints: The circumference is : 31.42

