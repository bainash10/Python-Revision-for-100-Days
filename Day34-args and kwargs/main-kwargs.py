 # *args = allows you to pass multiple non-key arguments
 # **kwargs = allows you to pass multiple keyword-arguments
 #          *      unpacking operator
 #!     1.positional    2. default      3. keyword  4. ARBITRARY 

def print_address(**kwargs):
    print(type(kwargs)) #packs into dictionary
    print()
    #! there are different built-in methods in **kwargs
    for values in kwargs.values():
        print(values)

    print()

    for key in kwargs.keys():
        print(key)

    print()

    for key, value in kwargs.items():
        print(f"{key}=>{value}")

    print()


    

print_address(street="123", city="New York", state="MI", zip="123")

print_address(street="444", city="Sydney")
