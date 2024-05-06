import time

# print(time.ctime(0))
#* convert a time expressed in seconds since epoch to a readable string
#* epoch = when your computer thinks time began (reference point)


# print(time.time())  #* return current seconds since epoch


# print(time.ctime(time.time()))

#!                                 EXAMPLE 1
#! time.strftime(format, time_object) = formats a time_object to a string
# time_object=time.localtime()  #! Local Time
# # print(time_object)
# local_time=time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)


# time_object=time.gmtime()   #! UTC time
# print(time_object)


#!                                 EXAMPLE 2
#! time.strptime(time_string, format) = parses a string representing time/date and returns a struct_time object
# time_string="6 May, 2024"
# time_object=time.strptime(time_string,"%d %B, %Y")
# print(time_object)




#!                                 EXAMPLE 3
#! time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
#! (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
# time_tuple=(2024,5,20,4,20,0,0,0,0)
# time_string= time.asctime(time_tuple)
# print(time_string)




#!                                 EXAMPLE 4
#! time.mktime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
#! (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple=(2024,5,20,4,20,0,0,0,0)
time_string= time.mktime(time_tuple)
print(time_string)