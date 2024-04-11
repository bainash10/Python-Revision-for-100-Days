 #* Prevents a user from creating an object of that class
 #* + compels a user to override abstract methods in a child class
 #* Its an Idea not a method
 #* abstract class = a class which contains one or more abstract methods.
 #* abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod  #!abc stands for abstract base class

class Vehicle(ABC): #! abstract class

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
        
    @abstractmethod
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the Motorcycle")

    @abstractmethod
    def stop(self):
        print("This motorcycle is stopped")

# vehicle=Vehicle()  #will show error as abstract class implementation cannot be done
car=Car()
motorcycle=Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()