 #* Higher Order Function =  a function that either:
 #*                          1. accepts a function as an argument
 #*                             or
 #*                          2. returns a function
 #*                          (In python, functions are also treated as objects)


#! 1. accepts a function as an argument

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")  #Here func can be loud or quiet in this example its like naming a function externally
    print(text)

hello(loud)
hello(quiet)
# hello(qiet) #! Prints error