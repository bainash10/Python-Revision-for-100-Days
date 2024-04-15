def hello():
    print("hello")

hello() #! Normal method to call a function

print(hello) #! Prints--> <function hello at 0x000001E72F2F3E20>  which is memory address where the function is located

hi = hello
print(hi)  #! Prints--> <function hello at 0x0000022F9C462B90> i.e. hello and hi memory address will be same

hi()  #can be used to call hello function by assigining memory address of hello to hi so we can treat hi as function