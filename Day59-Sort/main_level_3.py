#* Given is tuple of tuples
students=(("Nischal","A",1),
          ("Baidar","B",2),
          ("Ram","C",3),
          ("Shyam","D",4))

grade = lambda grades:grades[1]

sorted_students=sorted(students,key=grade)

for i in sorted_students:
    print(i)