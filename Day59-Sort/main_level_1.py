 #! sort() method   = used with lists
 #! sort() function = used with iterables

#Example 1: Sorting list ascending
students=["Nischal","Baidar","Ram","Shyam"]

students.sort()

for i in students:
    print(i)

#Example 2: Sorting list descending
print()
students=["Nischal","Baidar","Ram","Shyam"]

students.sort(reverse=True)

for i in students:
    print(i)


#Example 3: Sorting tuple ascending 
print()
students=("Nischal","Baidar","Ram","Shyam") 

#students.sort(reverse=True)  --> In Tuple this sort method wont work we require sorting function

sorted_students=sorted(students)

for i in sorted_students:
    print(i)


#Example 4: Sorting tuple descending
print()
students=("Nischal","Baidar","Ram","Shyam") 

#students.sort(reverse=True)  --> In Tuple this sort method wont work we require sorting function

sorted_students=sorted(students,reverse =True)

for i in sorted_students:
    print(i)
