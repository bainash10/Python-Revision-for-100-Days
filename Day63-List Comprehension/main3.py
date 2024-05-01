 #* list comprehension =  a way to create a new list with less syntax
 #*                       can mimic certain lambda functions, easier to read
 #*                       list = [expression for item in iterable]
 #*                       list = [expression for item in iterable if conditional]
 #*                       list = [expression if/else for item in iterable]


#! Using if else statement
#* list = [expression if/else for item in iterable]

students = [100,90,80,70,60,50,40,30,0]

passed_students=[i if i>=60  else "FAILED" for i in students ]

print(passed_students)