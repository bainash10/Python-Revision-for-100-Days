 # *method chaining = calling multiple methods sequentially
 # *                 each call performs an action on the same object and returns self


class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turned off the engine")
        return self



car=Car()

#! Normally to call a multiple function we use as follow:
#! car.turn_on()
#! car.drive()

#TODO:     Using Method Chaining-->use multiple call functions at same object at once and always remember the functions should have the statement: return self
car.turn_on().drive()  #! If only used this python will show error message : 'NoneType' error so need to keep return self in each and every functions

print()

car.brake().turn_off()


print()

car.turn_on().drive().brake().turn_off()

print()
print("_____If using multiple method chaining: then to read the code properly you can use the backslash character '\\' followed by enter everytime with '.'_____")
print()

car.turn_on()\
    .drive()\
        .brake()\
            .turn_off()