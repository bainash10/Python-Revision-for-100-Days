try:
    with open("Day39-Read a file/test.tx") as file: #with open closes the file automatically for us, but this doesnot handle and catch exceptions automatically
        print(file.read())

except FileNotFoundError:
    print("That file was not found ;(")

# print(file.closed)