 # *args = allows you to pass multiple non-key arguments
 # **kwargs = allows you to pass multiple keyword-arguments
 #          *      unpacking operator
 #!     1.positional    2. default      3. keyword  4. ARBITRARY 


#! usual functions: 

# def add(a,b):
#     return a+b

# print(add(1,2)) #prints 3

# print(add(1,2,3)) #prints error

#! Now to send varrying arguments we can use *args

def add(*args):  #*args can be named as *nums  that means succedding letters can be anything after *, for eg: " *nums " also can be written --> instead of *args 
    print(type(args))  #packs everything passed as argument to tuple
    total = 0
    for arg in args:
        total+= arg
    return total

print(add(1,2))

print(add(1)) 

print(add(1,2,3,4,5)) 
