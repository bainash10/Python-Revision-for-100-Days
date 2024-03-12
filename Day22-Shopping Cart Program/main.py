 # * Shopping cart program:

foods=[]
prices=[]
total=0

while True:
    food = input("Enter a food to buy: (q to quit): ")
    if food.lower() =="q":  
        #if tries capital q then it will temporarily change to small q and checks the condition.
        break
    else:
        price=float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart -----")

for food in foods:
    print(food, end=" ") #prints the items on single line with space as used: end=" "

for price in prices:
    total = total + price

print() #new line code
print(f"Your total is: ${total}")