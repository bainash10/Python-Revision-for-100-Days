 #* duck typing = concept where the class of an object is less important than the methods/attributes
 #*               class type is not checked if minimum methods/attributes are present
 #*               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwaking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck=Duck()
chicken=Chicken()
person=Person()

person.catch(duck)
print()
person.catch(chicken)

