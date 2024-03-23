 #* keyword arguments = an argument preceded by an identifier
#* helps with readability
#* order of arguments doesn't matter
#* 1.positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "Mr.", "Spongebob", "Squarepants")
hello("Squarepants","Mr.","Hello",  "Spongebob")

hello("Hello", title="Mr.", first="Spongebob", last="Squarepants")
hello(last="Squarepants", title="Mr.", greeting="Hello", first="Spongebob")
