# Logical Operators are used on conditional statements
# and = checks 2 or more condn are True
# or = checks if at least one condn is true
# not = true if condn is false and vice versa

temp = 25
if(temp>0 and temp<30): #t and t
    print("The temperature is good")
else:
    print("The temperature is bad")

temp = 25
if(temp<=0 or temp<=30): #f and t
    print("The temperature is good")
else:
    print("The temperature is bad")

#Normal:
sunny=True
if sunny==True:   #can be written as if sunny:
    print("It is sunny outside") #prints It is sunny outside
else:
    print("It is cloudy outside")

    #Using Not Operator:
sunny=True
if not sunny:   #can be written as if not sunny==True:
    print("It is sunny outside") #prints It is sunny outside
else:
    print("It is cloudy outside")