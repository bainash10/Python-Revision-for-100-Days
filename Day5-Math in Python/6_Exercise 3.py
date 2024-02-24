#Exercise: Hypotenuse calculator

import math

perpendicular=float(input("Enter the length of perpendicular: "))
base=float(input("Enter the length of base: "))

hypotenuse=math.sqrt(pow(perpendicular,2)+pow(base,2))
print(f"The length of the hypotenuse is: {round(hypotenuse,2)} ")