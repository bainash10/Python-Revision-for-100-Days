class Car:

    wheels=4 #class variable

    #The class variables are declared inside the class and outside a constructor

    def __init__(self,make,model,year,color):
        #instance variable is declared inside a constructor and can be given unique values
        self.make=make #instance variable
        self.model=model #instance variable
        self.year=year #instance variable
        self.color=color #instance variable