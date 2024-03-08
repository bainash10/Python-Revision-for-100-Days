rows= int(input("Enter the no of rows:"))
columns= int(input("Enter the no of columns:"))
symbol= input("Enter the symbol to use:")


for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
    