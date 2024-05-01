 #* list comprehension =  a way to create a new list with less syntax
 #*                       can mimic certain lambda functions, easier to read
 #*                       list = [expression for item in iterable]
 #*                       list = [expression for item in iterable if conditional]
 #*                       list = [expression if/else for item in iterable]

#! Filtering using Lmabda Function
students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)


print()

#! Filtering using List Comprehension
#* list = [expression for item in iterable if conditional]
passed_students=[i for i in students if i>=60]
print(passed_students)