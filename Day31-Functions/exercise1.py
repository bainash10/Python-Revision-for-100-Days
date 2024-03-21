def display(username,amount,due_date):
    print(f"hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
    print()

display("Nischal", 50, "01/01")
display("Baidar", 10, "01/02")