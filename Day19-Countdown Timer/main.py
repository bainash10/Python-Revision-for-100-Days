import time

my_time= int(input("Enter the time in seconds: "))

for x in reversed(range(0,my_time)):  #can also be written as:--> for x in range(my_time,0,-1) -->where -1 is a step
    seconds=x%60
    minutes= int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}") #The :02 inside each placeholder is a formatting specifier. It means that the variable should be formatted as an integer with at least two digits, and if the value has fewer than two digits, leading zeros should be added.
    time.sleep(1) #prints another result in 1 seconds delay
    

print("Time's up!")