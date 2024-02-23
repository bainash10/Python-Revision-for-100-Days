#Exercise name: Shopping cart

item=input("What item would you like to buy")
price=float(input("What is the price of that item"))
quantity=int(input("What many would you like to buy"))

total= price*quantity

print(f"You have bought {quantity} X {item}/s")
print(f"Your total is: ${total}") 
print(f"Your total is: ${round(total,2)}") #rounds to 2 decimal places
