 #* format specifiers ={value:flags} format a based on what flags are inserted
#Some of the flags are:
#? :(number)f = round to that many decimal places (fixed point)
#? :(number) = allocate that many spaces
#! :03 = allocate and zero pad that many spaces
#! :< = left justify
#! :> = right justify
#! :^ = center align
#* :+ = use a plus sign to indicate positive value
#* := = place sign to leftmost position
#* :  = insert a space before positive numbers
#* :, = comma separator

price1= 30.14159
price2= -9870.65
price3= 12.34

print(f"Price 1 is ${price1:.2f}") #prints 2 decimal places 3.14
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

print(f"Price 1 is ${price1:10}") #prints    3.14159 with 10 spaces 
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

print(f"Price 1 is ${price1:010}") #prints 0003.14159 with 0 padded
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

print(f"Price 1 is ${price1:<10}") #Left justified  --> Price 1 is $3.14159
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

print(f"Price 1 is ${price1:>10}") #Right justified --> Price 1 is $   3.14159
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

print(f"Price 1 is ${price1:^10}") #Center Align --> Price 1 is $ 3.14159
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

print(f"Price 1 is ${price1:+}") #To indicate Positive value --> Price 1 is $+3.14159
print(f"Price 2 is ${price2:+}") #Price 2 is $-987.65
print(f"Price 3 is ${price3:+}")

print(f"Price 1 is ${price1: }") #To insert a space before positive numbers --> Price 1 is $ 3.14159
print(f"Price 2 is ${price2: }") #Price 2 is $-987.65
print(f"Price 3 is ${price3: }")


price1= 30000000.14159
price2= -9870.65
price3= 1200.34
print(f"Price 1 is ${price1:,}") #Each 1000 places is separated with comma --> Price 1 is $3,000.14159
print(f"Price 2 is ${price2:,}") #Price 2 is $-9,870.65
print(f"Price 3 is ${price3:,}")


#* MIX AND MATCH FORMAT SPECIFIERS:
print(f"Price 1 is ${price1:+,.2f}") 
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")