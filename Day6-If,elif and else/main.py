# If - Do some code only if some condition is true
# Else - do something else
# Used in decision making

age = int(input("Enter your age: "))


if age>=100:
    print("You are too old to sign up")

elif (age>=18):   #if age>=18 can also be written
    print("You are now signed up")

elif age<0:
    print("You haven't been born yet")

else:
    print("You must be 18+ to sign up")