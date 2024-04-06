 #* multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism: #grandparent
    alive = True

class Animal(Organism): #parent
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog=Dog() #creating object dog from Dog() class
print(dog.alive)
dog.eat()
dog.bark()