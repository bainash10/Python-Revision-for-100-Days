from car import Car

car_1=Car("Chevy","Corvetter","2021","blue")
car_2=Car("Ford","Mustang","2024","red")


print(car_1.wheels)
print(car_2.wheels)
print()

car_1.wheels = 2 #changes only car_1 wheels values

print(car_1.wheels)
print(car_2.wheels)

print()
print(Car.wheels)

print()
Car.wheels=2  #changes all cars values

print(car_1.wheels)
print(car_2.wheels)
