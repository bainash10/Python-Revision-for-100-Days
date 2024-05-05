 #!  ***********************************
 #!  if _name_ == '__main__'
 #!  ***********************************

 #!  Why tho?
 #!  1. Module can be run as a standalone program
 #!  or
 #!  2. Module can be imported and used by other modules

 #*Python interpreter sets "special variables", one of which is _name_
 #*Python will assign the _name_ variable a value of '__main__' if it's the initial module being run


# import main2

# print(__name__)

# print(main2.__name__)

def hello():
    print("Hello!")

if __name__ =='__main__':
    print("Running this module directly")

else:
    print("Running other module indirectly")