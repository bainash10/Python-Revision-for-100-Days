import time

def count(end,start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(3,1) #o/p---> 1 2 3 DONE!
print("-------------------------")
count(4) #o/p----> 0 1 2 3 4 DONE!