# indexing = accessing elements of a sequence using [] (indexing operator)
# [start:end:step]

credit_number="1234-5678-9012"
print(credit_number[0]) #prints 1
print(credit_number[1]) #" 2
print(credit_number[2]) #" 3 
print(credit_number[0:4]) #prints 1234
print(credit_number[:4]) #prints from 0 to 4
print(credit_number[5:9]) #prints 5678
print(credit_number[5:]) #prints from index 5 to end 5678-9012
# from end starts indexing
print(credit_number[-1]) # Prints 2
print(credit_number[-2]) # Prints 1
print(credit_number[-3]) # Prints 0
print(credit_number[::2]) # Prints 13-6891
print(credit_number[::3]) # Prints 146-1

last_digits=credit_number[-4:]
print(f"XXXX-XXXX-{last_digits}")
