#Typecasting=The process of converting a value of one datatype to another
# (string, int, float, boolean)
# Explicit vs Implicit

name="Nischal"  #str
age=12 #int
gpa=3.5 #float
student=True #boolean

#Using type() function can give the type of the variable
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))


#explicit typecasting--> Manually changing the type of variable
age = float(age)  
print(age)  
print(type(age))   ###prints float###

gpa= int(gpa)
print(gpa)

student=str(student)
print(student)  
print(type(student))

age=bool(age)
print(age)  #prints age is True if anything other than 0 will print True

x=""
print(bool(x)) #prints false as it is empty string and converted to bool

x=" "
print(bool(x)) #If there is any space it will show true


#Implicit Typecasting-->Converted to another datatype automatically by interpreter
#Example:
x=2
y=2.0
x=x/y
print(x) 