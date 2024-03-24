 # *args example

def display_name(*args):
    for arg in args:
        print(arg, end= " ")
    print()

display_name("Nischal","Baidar")
display_name("Mr. ","Baidar", "Nischal")
display_name("Dr. ","Spongebob", "SquarePants", "Nick")