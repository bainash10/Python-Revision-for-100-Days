 #* exception =   events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    

except ZeroDivisionError as e: #* When divides by 0
    print(ZeroDivisionError)  #! prints--> <class 'ZeroDivisionError'>
    print(e) #! prints--> division by zero
    print("You can't divide by zero! ")

except ValueError as e: #* when divides by some string
    print(ValueError) #! prints--> <class 'ValueError'>
    print(e) #! prints--> invalid literal for int() with base 10: 'sad'
    print("Enter only numbers please")

except Exception: #!Not considered a good practice when used directly this specific exception handling because it directly handles every exceptions, so a good practice is to always try to handle specific exceptions.
    print("Something went wrong :(")

else:
    print(result)

finally:
    print("This will always execute and used for executing other code snippets other than inside exception handling")