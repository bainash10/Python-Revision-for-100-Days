#Exercise Name: Area of a circle

import math

radius = float(input("Enter the radius of a circle: "))

area= math.pi * radius**2  #can use pow(radius,2)
print(round(area,2))