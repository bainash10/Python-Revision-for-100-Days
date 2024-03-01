name= input("Enter your full name: ")

print(len(name)) #includes space too #gives length of the strings inputed

result=name.find("a") #finds the first occurence in string with character a
#starts from a
#index starts from 0
#if doesnot find character then it returns -1
print(result)

result = name.rfind("o") #last occurence of character o
print(result)

name=name.capitalize() #capitalize the first character of string
print(name)

name=name.upper() #all characters are upper case
print(name)

name=name.lower() #all characters are lower case
print(name)

result=name.isdigit() #true if string contains only digits, false if ab12 or abc
print(result)

result=name.isalpha() #true if string contains only alphabets, false if ab12 or 123
print(result)

