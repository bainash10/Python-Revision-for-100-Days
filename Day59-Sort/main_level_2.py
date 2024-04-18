 #! Using the name to sort in alphabetical order 
#* Given is list of tuples
students=[("Nischal","A",1),
          ("Baidar","B",2),
          ("Ram","C",3),
          ("Shyam","D",4)]


students.sort() 

for i in students:
    print(i)


 #! Using the name to sort in alphabetical order descending
print()
students=[("Nischal","A",1),
          ("Baidar","B",2),
          ("Ram","C",3),
          ("Shyam","D",4)]


students.sort(reverse=True) 

for i in students:
    print(i)


 #! Using the grades to sort in ascending order
print()
students=[("Nischal","C",1),
          ("Baidar","A",2),
          ("Ram","B",3),
          ("Shyam","D",4)]

grade = lambda grades:grades[1]
students.sort(key=grade) 

for i in students:
    print(i)

 #! Using the grades to sort in descending order
print()
students=[("Nischal","C",11),
          ("Baidar","A",22),
          ("Ram","B",33),
          ("Shyam","D",44)]

grade = lambda grades:grades[1]
students.sort(key=grade,reverse=True) 

for i in students:
    print(i)


 #! Using the age to sort in ascending order
print()
students=[("Nischal","C",1),
          ("Baidar","A",2),
          ("Ram","B",3),
          ("Shyam","D",4)]

age = lambda ages:ages[2]
students.sort(key=age) 

for i in students:
    print(i)


 #! Using the age to sort in reverse order
print()
students=[("Nischal","C",1),
          ("Baidar","A",2),
          ("Ram","B",3),
          ("Shyam","D",4)]

age = lambda ages:ages[2]
students.sort(key=age,reverse=True) 

for i in students:
    print(i)

