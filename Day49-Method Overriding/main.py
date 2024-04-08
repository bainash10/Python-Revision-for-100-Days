class Animal:

    #! overriden method
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    #! overriding method
    def eat(self): 
        print("This rabbit is eating a carrot")

rabbit=Rabbit()
rabbit.eat()  #o/p --> This rabbit is eating a carrot
#* the printing of output will always use a method that is more closely associated with itself first before relying on a method that it may inherit from a parent class