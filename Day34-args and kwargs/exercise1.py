#Using both *args and **kwargs

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    # for value in kwargs.values():
    #     print(value, end=" ")

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('zip')}")
    print(f"{kwargs.get('name')}") #prints none if no parameters


shipping_label("Dr.","Spongebob","Squarepants",
               street="123",
               city="Detroit",
               zip="674268")