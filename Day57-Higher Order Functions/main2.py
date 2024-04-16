 #* Higher Order Function =  a function that either:
 #*                          1. accepts a function as an argument
 #*                             or
 #*                          2. returns a function
 #*                          (In python, functions are also treated as objects) 

#! 2. returns a function


#! lets take an example 10/2 = 5 here 10 is dividend, 2 is divisior and 5 is quotient
def divisor(x):  #x=2 is stored from line 16
    def dividend(y):
        return y/x
    return dividend  #as this is returned when line 16 is worked so divide is assigned dividends memory location

divide= divisor(2) #x=2
print(divide(10)) #y=10  and divide is pointing dividends memory location