unit = input("Is this temparature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9)/5+32,1)  #(C*9/5)+32=degree fahrenheit
    print(f"The temperature in Fahrenheit is: {temp}degreeF")
elif unit == "F":
    temp = round((temp -32)*5/9,1) #(F-32)*5/9=degree celcius
    print(f"The temperature in Fahrenheit is: {temp}degreeC")
else:
    print(f"{unit} is an invalid of measurement")