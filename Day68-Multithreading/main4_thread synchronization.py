#Thread Synchronization

#Creating Thread

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(2)
    print("You studied!")


#Creating additional Thread:
x=threading.Thread(target=eat_breakfast, args=())
x.start()

#Creating additional Thread:
y=threading.Thread(target=drink_coffee, args=())
y.start()

#Creating additional Thread:
z=threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count()) #counting the number of threads that are running
print(threading.enumerate())  #prints list of all the threads that are running
print(time.perf_counter())


    