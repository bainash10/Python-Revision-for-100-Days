import random

# print(help(random))

low=1
high=100
options=("rock", "paper", "scissors")
cards=["2","3","4","J","Q","K","A"]

# number=random.randint(1,6) #* provides random int from random module into number variable from integers 1 to 6

#!can also write variable names until it has the value assigned in it
# number=random.randint(low,high)
# print(number)

# number=random.random() #!provides random number from 0 to 1 interval
# print(number)

# option=random.choice(options) #!great methods for games
# print(option)

random.shuffle(cards) #suffles the items inside cards variable
print(cards)
