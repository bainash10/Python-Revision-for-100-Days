# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)


#!Converting dollars to euros
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros=lambda data: (data[0],data[1]*0.82)
to_rupees=lambda data: (data[0],data[1]*127)

store_euros=list(map(to_euros,store))
store_rupees=list(map(to_rupees,store))

#! In euros
for i in store_euros:
    print(i)
    
print()

#! In rupees
for i in store_rupees:
    print(i)