class Car:
    
   
    def __init__(self,make,model,year,color):  #constructors, self is passed automatically
        self.make = make
        self.model = model
        self.year= year
        self.color=color


    def drive(self):
        print("This "+self.model+" car is driving")

    def stop(self):
        print("This "+self.model+" car is stopped")

